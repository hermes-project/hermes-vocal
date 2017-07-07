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


def result():
    return(Skill.randomAnswer(["bonjour !",
           "Salut !",
           "Bien le bonjour, humain !"]))

Skill.addSkill(keywords, result)


keywords = ["imite le dindon"]



def result():
    return(Skill.randomAnswer(["Glouglouglouglou"]))

Skill.addSkill(keywords, result)

keywords = ["TSP"]



def result():
    return(Skill.randomAnswer(["TSP il fallait l'inventé SP"]))

Skill.addSkill(keywords, result)

keywords = ["TEM"]

def result():
    return(Skill.randomAnswer(["TEM, comme dirait Jean-Pierre Coffe, C'est de la merde"]))

Skill.addSkill(keywords, result)
