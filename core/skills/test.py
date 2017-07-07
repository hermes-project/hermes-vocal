# Skill Test
from core.skills import Skill

keywords = ["test"]

results = ["Test ? Allo ?",
           "Test, 1, 2, Test !",
           "test réussi !"]

def result():
    return(Skill.randomAnswer(results))

Skill.addSkill(keywords, result)