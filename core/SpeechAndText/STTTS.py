from gtts import gTTS
import os


def tts(string):
    if len(string) != 0:
        ttsg = gTTS(text=string, lang='fr')
        ttsg.save("good.mp3")
        os.system("mpg321 good.mp3 2> /dev/null")

