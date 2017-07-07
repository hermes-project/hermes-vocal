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


keywords = ["imite le dindon"]

results = ["Glouglouglouglou"]

def result():
    return(Skill.randomAnswer(results))

Skill.addSkill(keywords, result)

keywords = ["TSP"]

results = ["TSP il fallait l'inventé SP"]

def result():
    return(Skill.randomAnswer(results))

Skill.addSkill(keywords, result)

keywords = ["TEM"]

results = ["TEM, comme dirait Jean-Pierre Coffe, C'est de la merde"]

def result():
    return(Skill.randomAnswer(results))

Skill.addSkill(keywords, result)
