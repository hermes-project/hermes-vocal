from tkinter import *
from tkinter import messagebox

import json


# Callbacks

def close():
    root.destroy()

def askClose():
    if(messagebox.askyesno("Quit", "Voulez vous sauvegarder ?")):
        save()
        close()
    else:
        close()


def suppressSkill(skillzone, listElement):
    print(listElement[0].get(1.0, "end-1c"))
    skillZoneList.remove(listElement)
    skillzone.pack_forget()

def newSkill():
    skillzone = LabelFrame(fenetre)
    skillzone.pack()

    key = Text(skillzone, width=40, height=10)
    superwords = Text(skillzone, width=40, height=10)
    badwords = Text(skillzone, width=40, height=10)
    responses = Text(skillzone, width=40, height=10)

    skillZoneList.append([key, superwords,badwords, responses])

    Button(skillzone, text="Supprimer",
           command=lambda skillZoneL=skillzone, keyPhrasesTextL=key, superWordTextL=superwords,badwordsTextL = badwords,
                          responsesTextL=responses: suppressSkill(skillZoneL,
                                                                      [keyPhrasesTextL, superWordTextL, badwordsTextL,responsesTextL])
           ).pack(side=RIGHT)

    key.pack(side=LEFT)
    superwords.pack(side=LEFT)
    badwords.pack(side=LEFT)
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
            localkeyphrases = getSeparatedStrings(skillzone[0])
            localsuperwords = getSeparatedStrings(skillzone[1])
            localbadwords = getSeparatedStrings(skillzone[2])
            localresponses = getSeparatedStrings(skillzone[3])
            if(localkeyphrases and localresponses):   # On ne vérifie pas qu'il y ait de superwords car c'est optionnel
                new['keyPhrases']= localkeyphrases
                new['superWords']= localsuperwords
                new['badWords'] = localbadwords
                new['responses']= localresponses
                newlist.append(new)
            else:
                messagebox.showerror(title="Impossible de sauvegarder une case vide !")
                break

        data = {}
        data['skillList'] = newlist
        jsonString = json.dumps(data, ensure_ascii=False)
        #TODO : Auto indentation ?

        print(jsonString)
        data_file.write(jsonString)

def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

###

root = Tk()

canvas = Canvas(root, borderwidth=0, background="#ffffff", width=1400, height=800)
fenetre = Frame(canvas, background="#ffffff", width=1400, height=800)
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
hsb = Scrollbar(root, orient="horizontal", command=canvas.xview)
canvas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

def mouse_wheel(event):
    if event.num == 5 or event.delta == -120:
        canvas.yview("scroll", 1, "units")
    if event.num == 4 or event.delta == 120:
        canvas.yview("scroll", -1, "units")


    return "break"

root.bind("<Button-4>", mouse_wheel)
root.bind("<Button-5>", mouse_wheel)




vsb.pack(side=RIGHT, fill="y")
hsb.pack(side=BOTTOM, fill="x")
canvas.pack(side="left", fill="both", expand="True")
canvas.create_window((4, 4), window=fenetre, anchor="nw")

fenetre.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

intro = LabelFrame(fenetre, text="Skill Editor for Hermes-Vocal")
Button(intro, text="Quit", command=askClose).pack(side=RIGHT)
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

        keyPhrasesText=Text(skillZone, width=40, height=10)
        for keyphrase in skill["keyPhrases"] :
            keyPhrasesText.insert(END, keyphrase+"\n")
        superWordsText=Text(skillZone, width=40, height=10)
        for superword in skill["superWords"] :
            superWordsText.insert(END, superword+"\n")

        badWordsText = Text(skillZone, width=40, height=10)
        for badword in skill["badWords"]:
            badWordsText.insert(END, badword + "\n")

        responsesText=Text(skillZone, width=40, height=10)
        for response in skill["responses"] :
            responsesText.insert(END, response+"\n")

        Button(skillZone, text="Supprimer", command=lambda skillZoneL=skillZone,keyPhrasesTextL=keyPhrasesText,superWordTextL=superWordsText,badWordsTextL=badWordsText,responsesTextL=responsesText: suppressSkill(skillZoneL, [keyPhrasesTextL, superWordTextL,badWordsTextL, responsesTextL])
               ).pack(side=RIGHT)

        skillZoneList.append([keyPhrasesText, superWordsText,badWordsText, responsesText])

        keyPhrasesText.pack(side=LEFT)
        superWordsText.pack(side=LEFT)
        badWordsText.pack(side=LEFT)
        responsesText.pack(side=LEFT)


load()

intro.pack(side=BOTTOM)


root.mainloop()

