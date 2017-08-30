# Skill pour demander au robot une info sur wikipedia

import re
import wikipedia
from core.skills.ArgSkill import ArgSkill
from core.utils.cleanString import cleanString
from core.communication import *
import core.utils.client as clientglobal

phrases = [
    "parle moi de",
    "parles moi de",
    "que sais tu sur",
    "que sais tu de",
    "que peux tu me dire sur",
    "que peux tu me dire à propos de",
    "que peux tu dire sur",
    "qu'est-ce que tu sais sur",
    "qu'est-ce que tu sais à propos de",
    "quelle est la définition de",
    "cherche la définition sur wikipedia de",
    "cherche sur wikipedia"
]

words = [

]

badwords = [

]

def response(order):

    order = cleanString(order)
    for phrase in phrases:
        phrase = cleanString(phrase)
        if phrase in order:
            order = re.sub(phrase, '', order)

            if globalclient.currentJson["type"] == "confirmation": # Si l'ordre est déjà une confirmation :
                if isConfirmation(globalclient.currentJson["answer"]): # On vérifie si la personne a dit "oui" ou "non"
                    wikipedia.set_lang("fr")
                    return wikipedia.summary(order, sentences=1)
                else:
                    return ("Dommage ! j'en étais capable...")
            else:
                askConfirmation("Voulez vous que je recherche "+order+" sur Wikipédia ?", clientglobal.currentJson["msg"], clientglobal.client)
                return ""

ArgSkill(phrases, words,badwords, response)