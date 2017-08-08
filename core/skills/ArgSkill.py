# Classe des requêtes avec des arguments potentiels (par ex : "Emmene moi ICI")

from core.skills.Skill import Skill


class ArgSkill(Skill):
    def ask(self, order):
        # Verification 1 : Phrase exacte
        for i in self.keyphrases:
            if (i in order):  # Modif par rapport au Skill normal
                return True
        return False

    def execute(self, order):
        return self.result(order)

    def __init__(self, keyphrases, superwords, result):
        super().__init__(keyphrases, superwords, result)
