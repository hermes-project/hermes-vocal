# Vocal interface

from core.SpeechAndText import STTTS

import logging
from core import core
#logging.basicConfig(level=logging.DEBUG)

print("######################")
print("#    Hermes-vocal    #")
print("######################")

while(42):
    order = input("Order : ")

    ret = core.executeSkill(order)

    print("\n"+ret)
    STTTS.tts(ret)

    print("\n--------------\n")
