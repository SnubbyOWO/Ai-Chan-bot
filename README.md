# Ai-Chan Discord Bot
This is a fork of Waifu Speech but instead uses discord bot to use TTS. If you do use this/use as a reference please give credit to me and mirchuigawa (original creater)

Ai-Chan is a Discord bot that offers gets the active users input and uses Voicevox API to create a TTS audio clip.

The bot is programmed to carry out certain activities including text translation and text to speech generation. These operations are carried out using a variety of APIs and libraries, including the Voicevox API for TTS audio and the Google Cloud Translate API for translation.

It will also message IF there is a error with something, such as a audio making clip but not all the time as if you dont put a high proccessing time number the bot will a .WAV file that has nothing and is 0 bytes

# Ai-Chan Discord Bot Commands

``` konsole
!about - about the bot

!commands - list of commands

!start - start the AI generation
```

# Video/Audio

https://user-images.githubusercontent.com/87741849/227775080-acfd8b4b-c522-49e1-9e8c-d3ebbab3de4c.mp4

Another Example:

https://user-images.githubusercontent.com/87741849/228070145-4054d60e-ecc1-4918-896c-131f50f14fe2.mp4

The text:

Heya! I am Snubby, or you can call me Snubs but im a developer and i love to code! Hahaha anyways i have to bounce! Eh? Whats the matter? Oh the voice? Yeah i put my self as a anime girl because why not you know? Kinda cute.

おい！ 私はスナブです、またはあなたは私をスナブと呼ぶことができますが、私は開発者であり、私はコーディングするのが大好きです！ とにかく私は跳ね返らなければなりません！ ええ〜？ どうしたの？ なんてこった？ ええ、私はアニメの女の子として自分自身を置きました。なぜあなたは知らないのですか？ ちょっとかわいい〜。

### How does Waifu Speech discord bot work?
It uses Discord.py and Voicevox to use the bot and read messages of the user then to create the voice/TTS. 

### How do I run this program
To run this you need to install the requirments, you need Python version 3.7++, so make sure you have Python installed on your computer.

#### Install modules
- Windows, Linux, Mac
``` konsole
pip install -r requirements.txt
```
*  I'm not sure it will work on all platforms but you can give it a try. I tried it on linux

If already installed
``` konsole
python3 bot.py
```
or
``` konsole
python bot.py
```
or again,
``` konsole
py bot.py
```
There is a changed main.py file as well that instead of using a audio file like the original you can just type it instead. So it could also just be a generator.

### License
[see: LICENSE](/LICENSE)
