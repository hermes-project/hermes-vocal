from gtts import gTTS
import os


def tts(string):
    if len(string) != 0:
        ttsg = gTTS(text=string, lang='fr')
        ttsg.save("good.mp3")
        os.system("mplayer good.mp3 1> /dev/null 2> /dev/null")

        command = "espeak \"" + string + "\" -v fr -s 140 1> /dev/null 2> /dev/null"
        os.system(command)
