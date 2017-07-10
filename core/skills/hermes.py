# Skill Hermes
from core.skills import Skill

keyphrases = ["qui es tu",
            "qui est tu",
            "qui tu es",
            "qui tu est"]

keywords = ["tu"]

def result():
    return("Je suis Hermes, une IA codée par deux génies")

Skill.addSkill(keyphrases, keywords, result)

keyphrases = ["qui sont tes créateurs",
            "qui sont tes createurs",
            "qui est ton créateur",
            "qui est ton createur"]

keywords = ["créateur","créateurs"]

def result():
    return("Mes créateurs sont Louis-Baptiste Trailin et Rémi Dulong")

Skill.addSkill(keyphrases, keywords, result)

keyphrases = ["bonjour",
            "salut"]

keywords = ["bonjour","salut"]

def result():
    return(Skill.randomAnswer(["bonjour !",
           "Salut !",
           "Bien le bonjour, humain !"]))

Skill.addSkill(keyphrases, keywords, result)


keyphrases = ["imite le dindon", "imite les dindons"]

keywords = ["dindon","imite","dindons"]

def result():
    return(Skill.randomAnswer(["Glouglouglouglou"]))

Skill.addSkill(keyphrases, keywords, result)

keyphrases = ["TSP", "tsp"]

keywords = ["TSP", "tsp"]

def result():
    return(Skill.randomAnswer(["TSP il fallait l'inventé SP",
                               "La seule chose à garder de TSP c'est INTech",
                               "De toute façon vous deviendrais consultant ici"]))

Skill.addSkill(keyphrases, keywords, result)

keyphrases = ["TEM", "tem"]

keywords = ["TEM", "tem"]

def result():
    return(Skill.randomAnswer(["T E M, comme dirait Jean-Pierre Coffe, C'est de la merde",
                               "T E M ce n'est pas une vrai école, ce n'est que de la poudre de perlimpinpin",
                               "T E M, on vous encule !!! hashtag R P Z le roux des républicains"]))

Skill.addSkill(keyphrases, keywords, result)

keyphrases = ["TARDIS","tardis"]

keywords = ["TARDIS", "tardis"]

def result():
    return(Skill.randomAnswer(["Le tardis est l'acronime anglais de (Time and Relative Dimention In Space)",
                               "exterminate !!",
                               "delete"]))

Skill.addSkill(keyphrases, keywords,result)
