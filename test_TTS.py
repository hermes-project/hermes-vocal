from gtts import gTTS
import os




while(True) :
    order = input("Order : ")
    if (len(order) != 0) :

        tts = gTTS(text=order, lang='fr')
        tts.save("good.mp3")
        os.system("mplayer good.mp3 1> /dev/null 2> /dev/null")

