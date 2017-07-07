from gtts import gTTS
import os




while(True) :
    order = input("Order : ")
    if (len(order) != 0) :

        tts = gTTS(text=order, lang='fr')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")

