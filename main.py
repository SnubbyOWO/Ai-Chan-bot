import translators.server as tss
import requests
import speech_recognition as sr

# instead of using audio clips now just type it instead!
class AudioToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def convert(self):
        try:
            text = input("Enter your text: ")
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

    def generate_audio(self, speaker_id=2): # Change ID if you want
        try:
            url = f"https://api.tts.quest/v1/voicevox/?text={self.text}&speaker={speaker_id}"
            response = requests.get(url).json()
            if response["success"] == True:
                audio_url = response["mp3DownloadUrl"]
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
            return False

if __name__ == "__main__":
    # Create an instance of the AudioToText class and call the convert method to get user input
    audio_to_text = AudioToText()
    text = audio_to_text.convert()
    if not text:
        print("[Failed] Failed to convert audio file to text")
        exit()

    # Create an instance of the TextTranslator class and call the translate method
    translator = TextTranslator(text)
    translated_text = translator.translate("id", "ja")
    if not translated_text:
        print("[Failed] Failed to translate text")
        exit()

    # generate audio file
    text_to_speech = TextToSpeech(translated_text)
    audio_url = text_to_speech.generate_audio()
    if not audio_url:
        print("[Failed] Failed to generate audio")
        exit()

    # Save the audio file to disk
    file_name = "test.mp3"
    if text_to_speech.save_audio(audio_url, file_name):
        print(f"[Success] Audio file saved as {file_name}")
    else:
        print("[Failed] Audio file not saved")
