# Core of Hermes-vocal

from core.skills import Skill
from core.skills import *

def executeSkill(order):
    order.strip(',.').lower()
    for skill in Skill.SkillsList:
        if skill.ask(order):
            return(skill.execute())
    return("je ne comprend pas, pouvez vous répéter ?")


