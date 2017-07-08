# Skill Hermes
from core.skills import Skill

keywords = ["qui es tu",
            "qui est tu",
            "qui tu es",
            "qui tu est"]

def result():
    return("Je suis Hermes, une IA codée par deux génies")

Skill.addSkill(keywords, result)

keywords = ["qui sont tes créateurs",
            "qui sont tes createurs",
            "qui est ton créateur",
            "qui est ton createur"]

def result():
    return("Mes créateurs sont Jean-Baptiste Trailin et Rémi Dulong")

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
    return(Skill.randomAnswer(["TSP il fallait l'inventé SP",
                               "La seule chose à garder de TSP c'est INTech",
                               "De toute façon vous deviendrais consultant ici"]))

Skill.addSkill(keywords, result)

keywords = ["TEM"]

def result():
    return(Skill.randomAnswer(["T E M, comme dirait Jean-Pierre Coffe, C'est de la merde",
                               "T E M ce n'est pas une vrai école, ce n'est que de la poudre de perlimpinpin",
                               "T E M, on vous encule !!! hashtag R P Z le roux des républicains"]))

Skill.addSkill(keywords, result)
