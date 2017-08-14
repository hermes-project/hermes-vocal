# Skill pour demander au robot une info sur wikipedia

from core.skills.ArgSkill import ArgSkill
from core.utils.cleanString import cleanString
import re
import wikipedia

phrases = [
    "parle moi de",
    "parles moi de",
    "que sais tu sur",
    "que sais tu de",
    "que peux tu me dire sur",
    "que peux tu me dire à propos de",
    "que peux tu dire sur",
    "qu'est-ce que tu sais sur",
    "qu'est-ce que tu sais à propos de"
]

words = [

]

def response(order):

    order = cleanString(order)
    for phrase in phrases:
        if phrase in order:
            order = re.sub(phrase, '', order)
            wikipedia.set_lang("fr")
            return wikipedia.summary(order, sentences=1)
    return("Je n'ai pas compris ce que vous voulez savoir")

ArgSkill(phrases, words, response)