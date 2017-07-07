import random

SkillsList = []

class Skill:

    def __init__(self, keywords, result):
        self.keywords = keywords
        self.result = result

    def ask(self, order):
        for i in self.keywords:
            if (i == order):
                return True

        return False

    def execute(self):
        return(self.result())


def randomAnswer(answers):
    return(random.choice(answers))

def addSkill(keywords, result):
    skill = Skill(keywords, result)
    SkillsList.append(skill)