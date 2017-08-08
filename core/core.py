# Core of Hermes-vocal

from core.skills import skillsLoader
from core.utils.cleanString import cleanString


def executeSkill(order):  # Traitement d'un ordre (complexe)
    order = cleanString(order)
    orders = order.split(",")  # On regarde si on peut séparer l'ordre en 2 (si il y a une virgule)
    returns = []
    for ord in orders:
        returns.append(computeOrder(ord.lstrip().rstrip()) + "\n")
    finalreturn = ""
    for a in returns:
        finalreturn += a
    return finalreturn


def computeOrder(order):    # Traitement d'un ordre simple (splité)
    for skill in skillsLoader.SkillsList:
        if skill.ask(order):  # Si la phrase demandée est connue
            return skill.execute(order)

    scores = []  # Sinon, on calcule les scores de similarité
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

    if (secMaxSimilitude == maxSimilitude):
        print("2 phrases de même similarité !")
        return "Je ne comprends pas cette phrase."

    if (maxSimilitude == 0):  # Si on a aucun mot commun nulle part
        print("Pas de mot commun !")
        return "Je ne comprends pas cette phrase."

    if maxSimilitude > 5 * secMaxSimilitude:
        if (maxSimilitude >= 10):
            return (skillsLoader.SkillsList[maxSimilitudeIndex].execute(order))

    return ("Je ne comprends pas cette phrase")
