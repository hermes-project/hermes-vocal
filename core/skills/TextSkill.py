from core.skills.Skill import *

class TextSkill(Skill):

    def result(self):
        return (random.choice(self.results))

    def __init__(self, keyphrases, superwords, results):

        self.results = results
        super().__init__(keyphrases, superwords, self.result)


