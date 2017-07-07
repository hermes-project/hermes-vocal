# Skill Hermes
from core.skills import Skill

keywords = ["qui es tu",
            "qui est tu",
            "qui tu es",
            "qui tu est"]

def result():
    return("Je suis Hermes, une IA codée par deux génies")

Skill.addSkill(keywords, result)

keywords = ["bonjour",
            "salut"]

results = ["bonjour !",
           "Salut !",
           "Bien le bonjour, humain !"]

def result():
    return(Skill.randomAnswer(results))

Skill.addSkill(keywords, result)
