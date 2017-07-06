# Core of Hermes-vocal
from core import Skill
testSkill = Skill.Skill()

skills = [testSkill]

def findSkill(order):
    for skill in skills:
        if skill.ask(order):
            skill.execute()
            return
    print("Pouvez vous répéter ?")


def processOrder(order):
    print("processOrder : "+ order)
    findSkill(order)

