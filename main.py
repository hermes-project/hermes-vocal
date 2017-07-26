# Vocal interface

from core.SpeechAndText import STTTS

from core import core

print("######################")
print("#    Hermes-vocal    #")
print("######################")

while(42):
    order = input("Order : ")

    ret = core.executeSkill(order)

    print("\n"+ret)
    STTTS.tts(ret)

    print("\n--------------\n")
