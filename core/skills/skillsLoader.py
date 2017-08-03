import json
from pprint import pprint
import random

SkillsList = []

def randomAnswer(answers):
    return(random.choice(answers))

def addSkill(keywords, superwords,result):
    skill = Skill(keywords, superwords, result)
    SkillsList.append(skill)

def addTextSkill(keywords, superwords, results):
    skill = TextSkill(keywords, superwords, results)
    SkillsList.append(skill)



# Chargement des modules de Skills

from core.skills.Skill import *
from core.skills.TextSkill import *
from core.skills.TimeSkill import *

# Chargement des TextSkills depuis le json

with open('core/skills/phrases.json', encoding='utf-8') as data_file:
    data = json.load(data_file)

for skill in data["skillList"] :
    addTextSkill(skill["keyPhrases"], skill["superWords"], skill["responses"])



