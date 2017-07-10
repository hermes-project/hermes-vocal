# Skill Test
from core.skills import Skill

keywords = ["test"]

results = ["Test ? Allo ?",
           "Test, 1, 2, Test !",
           "test réussi !"]

word = ["test"]

def result():
    return(Skill.randomAnswer(results))

Skill.addSkill(keywords, word, result)