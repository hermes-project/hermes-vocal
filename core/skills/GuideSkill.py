# Skill pour demander au robot de nous guider

import json
import core.robot as robot
from core.skills.ArgSkill import ArgSkill
from core.utils.cleanString import cleanString

with open('core/map.json', encoding='utf-8') as data_file:
    map = json.load(data_file)

phrases = [
    "guide moi",
    "amène moi",
    "amene moi",
    "emmene moi",
    "ou est",
    "je veux aller",
    "je dois aller",
    "j'aimerai aller",
    "je voudrais aller",
    "va à",
    "va au"
]

words = [
    "guide",
    "amene",
    "emmene"
]

def response(order):

    for l in map["label"]:
        if cleanString(l["text"]) in order:
            
            robot.goto(l["text"])
            return("Je vous amène à "+l["text"])
    return("Je n'ai pas compris votre destination.")

ArgSkill(phrases, words, response)