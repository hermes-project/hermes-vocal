# Vocal interface

#from core.SpeechAndText import STTTS
from core.utils.logs import *

from core import core

logBold("######################")
logBold("#    Hermes-vocal    #")
logBold("######################")

while(42):
    order = input("Order : ")

    ret = core.executeSkill(order)

    logGreen("\n"+ret)
    #STTTS.tts(ret)

    logBlue("\n--------------\n")
