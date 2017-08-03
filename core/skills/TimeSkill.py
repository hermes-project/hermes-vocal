from core.skills import skillsLoader
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

skillsLoader.addSkill(phrases, words, result)
