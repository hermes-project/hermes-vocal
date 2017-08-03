# Core of Hermes-vocal

from core.skills import skillsLoader
from numpy import mean

def executeSkill(order):
    order.strip(',.').lower()
    for skill in skillsLoader.SkillsList:
        if skill.ask(order):
            return(skill.execute())

    scores = []
    for skill in skillsLoader.SkillsList:
        scores.append(skill.similitude(order))

    maxSimilitude = max(scores)
    maxSimilitudeIndex = scores.index(maxSimilitude)


    secScores = []
    secScores += scores
    secScores[maxSimilitudeIndex] = 0

    secMaxSimilitude = max(secScores)
    secMaxSimilitudeIndex = scores.index(secMaxSimilitude)

    print(scores)

    if(secMaxSimilitude == maxSimilitude) :
        print("2 phrases de même similarité !")
        return "Je ne comprend pas cette phrase."


    if(maxSimilitude == 0) : # Si on a aucun mot commun nulle part
        print("Pas de mot commun !")
        return "Je ne comprend pas cette phrase."





    if maxSimilitude > 5*secMaxSimilitude :
        if(maxSimilitude >= 10) :
            return(skillsLoader.SkillsList[maxSimilitudeIndex].execute())



    return("Je ne comprend pas cette phrase.")


