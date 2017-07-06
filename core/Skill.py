class Skill:

    def __init__(self):
        self.keywords = ["test"]

    def ask(self, order):
        for i in self.keywords:
            if (i == order):
                return True

        return False

    def execute(self):
        print("Test de Skill réussi !")