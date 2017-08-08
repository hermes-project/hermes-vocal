import random
from core.skills.skillsLoader import SkillsList

class Skill:

    def __init__(self, keyphrases,superwords, result):
        self.keyphrases = keyphrases
        self.superwords = superwords
        miscKeyPhrases = [wordPhrase.split() for wordPhrase in self.keyphrases]
        miscKeyWords = []
        for miscKeyphrase in miscKeyPhrases :
            miscKeyWords+=miscKeyphrase

        self.keywords = []
        for keyword in miscKeyWords :
            if keyword not in self.keywords :
                self.keywords.append(keyword)  # Séparation en mots clés uniques

        print("Skill loaded : "+self.keyphrases[0])
        self.result = result
        SkillsList.append(self)

    def ask(self, order):
        # Verification 1 : Phrase exacte
        for i in self.keyphrases:
            if (i == order):
                return True
        return False

    def similitude(self, order):
        # Vérification 2 : Proximité avec l'ordre
        orderWords = order.split()
        res = 0
        for orderWord in orderWords :
            ##print("Modele : " + orderWord)
            for keyword in self.keywords :
                ##print("test : "+keyword)
                if keyword == orderWord :
                    ##print("MATCH !!!")
                    if(keyword in self.superwords) :
                        res+=10
                    else :
                        res+=1
        return res


    def execute(self, *args):
        return(self.result())








from core.skills.ArgSkill import * # Ajoute le support des skills avec argument
