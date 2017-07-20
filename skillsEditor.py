from tkinter import *
from tkinter import messagebox

import json


# Callbacks

def close():
    global fenetre
    fenetre.destroy()

def askClose():
    if(messagebox.askyesnocancel("Quit", "Do you want to save ?")):
        print("TODO : SAVE")
        close()
    elif "cancel":
        pass
    else:
        close()

def lol (a):
    print(a)

def suppressSkill(skillzone, listElement):
    print(listElement[0].get(1.0, "end-1c"))
    skillZoneList.remove(listElement)
    skillzone.pack_forget()

def newSkill():
    skillzone = LabelFrame(fenetre)
    skillzone.pack()

    key = Text(skillzone, width=50, height=10)
    superwords = Text(skillzone, width=50, height=10)
    responses = Text(skillzone, width=50, height=10)

    skillZoneList.append([key, superwords, responses])

    Button(skillzone, text="Supprimer",
           command=lambda skillZoneL=skillzone, keyPhrasesTextL=key, superWordTextL=superwords,
                          responsesTextL=responses: suppressSkill(skillZoneL,
                                                                      [keyPhrasesTextL, superWordTextL, responsesTextL])
           ).pack(side=RIGHT)

    key.pack(side=LEFT)
    superwords.pack(side=LEFT)
    responses.pack(side=LEFT)


def getSeparatedStrings(skillZoneText):
    raw = skillZoneText.get(1.0, "end-1c")
    result = raw.split('\n')
    if "" in result :
        result = list(filter(None, result))
    return(result)

def save():
    with open('core/skills/phrases.json', 'w', encoding='utf-8') as data_file:

        newlist = []
        #newjson = data_file
        for skillzone in skillZoneList:
            new = {}
            new['keyPhrases']= getSeparatedStrings(skillzone[0])
            new['superWords']= getSeparatedStrings(skillzone[1])
            new['responses']= getSeparatedStrings(skillzone[2])
            newlist.append(new)

        data = {}
        data['skillList'] = newlist
        jsonString = json.dumps(data, ensure_ascii=False)
        #TODO : Auto indentation ?

        print(jsonString)
        data_file.write(jsonString)


###

fenetre = Tk()

scroll=Scrollbar(fenetre)
scroll.pack(side=RIGHT, fill=Y)

intro = LabelFrame(fenetre, text="Skill Editor for Hermes-Vocal")
Button(intro, text="Quit", command=close).pack(side=RIGHT)
Button(intro, text="Save", command=save).pack(side=RIGHT)
Button(intro, text="New Skill", command=newSkill).pack()

intro.pack(side=TOP)

with open('core/skills/phrases.json', encoding='utf-8') as data_file:
    data = json.load(data_file)


skillZoneList = []

def load():
    for skill in data["skillList"] :
        skillZone = LabelFrame(fenetre, text=skill["keyPhrases"][0])
        skillZone.pack()

        keyPhrasesText=Text(skillZone, width=50, height=10)
        for keyphrase in skill["keyPhrases"] :
            keyPhrasesText.insert(END, keyphrase+"\n")
        superWordsText=Text(skillZone, width=50, height=10)
        for superword in skill["superWords"] :
            superWordsText.insert(END, superword+"\n")
        responsesText=Text(skillZone, width=50, height=10)
        for response in skill["responses"] :
            responsesText.insert(END, response+"\n")

        Button(skillZone, text="Supprimer", command=lambda skillZoneL=skillZone,keyPhrasesTextL=keyPhrasesText,superWordTextL=superWordsText,responsesTextL=responsesText: suppressSkill(skillZoneL, [keyPhrasesTextL, superWordTextL, responsesTextL])
               ).pack(side=RIGHT)

        skillZoneList.append([keyPhrasesText, superWordsText, responsesText])

        keyPhrasesText.pack(side=LEFT)
        superWordsText.pack(side=LEFT)
        responsesText.pack(side=LEFT)


load()



fenetre.mainloop()

