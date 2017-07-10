import random

SkillsList = []

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

        print(self.keywords)
        self.result = result

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


    def execute(self):
        return(self.result())


class TextSkill(Skill):

    def result(self):
        return (random.choice(self.results))

    def __init__(self, keyphrases, superwords, results):

        self.results = results
        super().__init__(keyphrases, superwords, self.result)




def randomAnswer(answers):
    return(random.choice(answers))

def addSkill(keywords, superwords,result):
    skill = Skill(keywords, superwords, result)
    SkillsList.append(skill)

def addTextSkill(keywords, superwords,results):
    skill = TextSkill(keywords, superwords, results)
    SkillsList.append(skill)