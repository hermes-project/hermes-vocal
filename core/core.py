# Core of Hermes-vocal

from core.skills import Skill
from core.skills import *
from numpy import mean

def executeSkill(order):
    order.strip(',.').lower()
    for skill in Skill.SkillsList:
        if skill.ask(order):
            return(skill.execute())

    scores = []
    for skill in Skill.SkillsList:
        scores.append(skill.similitude(order))

    maxSimilitudeIndex = scores.index(max(scores))
    maxSimilitude = max(scores)
    for i in range(len(scores)) :
        if (scores[i] == maxSimilitude) and (i!=maxSimilitudeIndex): # Si on a 2 max similitude, pas la peine d'essayer !
            print("2 phrases de même similarité !")
            print(scores)
            return "Je ne comprend pas cette phrase."

    avgSimilitude = mean(scores)

    if avgSimilitude == 0 : # Si on a aucun mot commun nulle part
        print("Pas de mot commun !")
        return "Je ne comprend pas cette phrase."


    if maxSimilitude/avgSimilitude > 2 :
        return(Skill.SkillsList[maxSimilitudeIndex].execute())

    return("je ne comprend pas, pouvez vous répéter ?")


