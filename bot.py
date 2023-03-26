import translators.server as tss
import requests
import speech_recognition as sr
import discord
from discord.ext import commands
import asyncio

class AudioToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def convert(self, text):
        try:
            print(f"[Success] You say: {text}")
            return text
        except:
            return None

class TextTranslator:
    def __init__(self, text):
        self.text = text

    def translate(self, source, target):
        try:
            translated_text = tss.google(self.text, source, target)
            print(f"[Success] Translated: {translated_text}")
            return translated_text
        except:
            return None


class TextToSpeech:
    def __init__(self, text):
        self.text = text

    def generate_audio(self, speaker_id=2): # You can change the voice id to what you want
        try:
            url = f"https://api.tts.quest/v1/voicevox/?text={self.text}&speaker={speaker_id}"
            print(f"[Log] https://api.tts.quest/v1/voicevox/?text={self.text}&speaker={speaker_id}")
            response = requests.get(url).json()
            if response["success"] == True:
                audio_url = response["wavDownloadUrl"]
                print(f"[Success] Producing file")
                return audio_url
            else:
                return None
        except:
            return None

    def save_audio(self, audio_url, file_name):
        try:
            audio_content = requests.get(audio_url).content
            with open(file_name, "wb") as file:
                file.write(audio_content)
            return True
        except:
            print(f"[Failed] Producing file")
            return False

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Game(name="AI Voice Generation!"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!start'):
        await client.change_presence(activity=discord.Game(name="Generating AI Voice Currently!"))
        await message.channel.send("Please say your text:")
        text = await client.wait_for('message', check=lambda m: m.author == message.author)
        if not text:
            await message.channel.send("[Failed] Failed to convert audio file to text")
            return

        sleep_time = 5 

        lang = 'ja'

        #What lang lol
        await message.channel.send("[Wait] What Language? EN or JA (This was meant for Japanese but why not):")
        response = await client.wait_for('message', check=lambda m: m.author == message.author)
        if response.content == "EN":
            lang = 'en'
        else:
            lang = 'ja'

        # Ask how long the user wants the file to process or sm
        await message.channel.send("[Wait] Please enter the number of seconds to wait. Put '.' for default wait.\n(Longer time = More garentee file if text is long!):")
        response = await client.wait_for('message', check=lambda m: m.author == message.author)
        if response.content.isdigit():
            sleep_time = int(response.content)

        # Create an instance of the TextTranslator class and call the translate method
        translator = TextTranslator(text.content)
        translated_text = translator.translate("id", lang)
        if not translated_text:
            await message.channel.send("[Failed] Failed to translate text")
            return
        await message.channel.send(f"[Success] Translated: {translated_text}")

        # generate audio file
        text_to_speech = TextToSpeech(translated_text)
        audio_url = text_to_speech.generate_audio()
        if not audio_url:
            await message.channel.send("[Failed] Failed to generate audio")
            return

        # Save the audio file to disk
        file_name = "output.wav"

        # Processes the file before it just sends in a blank 0 byte file
        await message.channel.send(f"[Loading] Now please wait as the file processes {sleep_time} sec")

        await asyncio.sleep(sleep_time)

        if text_to_speech.save_audio(audio_url, file_name):
            await message.channel.send(file=discord.File(file_name))
            await message.channel.send(f"[Success] Audio file sent as {file_name}")
            print(f"[Success] Sending file")
            await client.change_presence(activity=discord.Game(name="AI Voice Generation!"))
        else:
            await message.channel.send("[Failed] Audio file not sent")
            print(f"[Failed] Audio file not sent")
            await client.change_presence(activity=discord.Game(name="AI Voice Generation!"))

    if message.content.startswith('!about'):
        description = "This is a translation bot that converts user's input text to Japanese anime girl voice using Voicevox. Although it isnt perfect, it at least works sometimes.\nOriginal Code: https://github.com/miruchigawa/Waifu-Speech \nModded By: https://github.com/snubbyowo"
        await message.channel.send(description)

    if message.content.startswith('!commands'):
        description = "!about - about the bot\n!commands - list of commands\n!start - start the AI generation"
        await message.channel.send(description)

client.run('DISCORDTOKENHERE')
