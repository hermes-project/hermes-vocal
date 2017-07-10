from core.skills import Skill
import json
from pprint import pprint

with open('core/skills/phrases.json', encoding='utf-8') as data_file:
    data = json.load(data_file)

for skill in data["skillList"] :
    Skill.addTextSkill(skill["keyPhrases"], skill["superWords"], skill["responses"])
