from core.skills import Skill
import datetime

# Gestion de l'heure :

phrases = [
    "quelle heure est-il",
    "quelle heure est il",
    "il est quelle heure",
    "c'est quelle heure"
]

words = [
    "heure"
]

def result():
    return "Il est " + datetime.datetime.now().strftime("%I") + " heures et " + datetime.datetime.now().strftime("%M") + " minutes"

Skill.addSkill(phrases, words, result)
