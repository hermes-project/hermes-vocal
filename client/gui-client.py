from tkinter import *
import socket as sck
import json

### Initialisation de l'interface graphique ###

root = Tk()
#fenetre = Frame(root, background="#ffffff", width=800, height=600)

def submitCallback():
    request = requestBox.get()
    if request != "":
        requestBox.delete(0, END)
        printRequest(request)
        askServer(request)


conversation = Text(root, width=50, height=40)
requestBox = Entry(root, width=40)
submitButton = Button(root, text="Submit", command=submitCallback)

def returnCallback(event):
    submitCallback()

root.bind('<Return>', returnCallback)

conversation.tag_add("request", END)
conversation.tag_add("robot", END)
conversation.tag_add("system", END)
conversation.tag_add("error", END)
conversation.tag_configure("request", justify="right", foreground="green")
conversation.tag_configure("robot", justify="left", foreground="blue")
conversation.tag_configure("system", justify="center")
conversation.tag_configure("error", justify="center", foreground="red")

def printRobot(str):
    conversation.insert(END, str+"\n", "robot")
def printRequest(str):
    conversation.insert(END, str+"\n", "request")
def printSystem(str):
    conversation.insert(END, str+"\n", "system")
def printError(str):
    conversation.insert(END, str+"\n", "error")



conversation.pack()
requestBox.pack()
submitButton.pack()

printSystem("-- Hermes Vocal --")


### Communication avec le serveur ###

#hote="172.16.84.9"
hote="localhost"
port = 15555
askConfirmation = False  # Variable globale pour savoir si on renvoie une confirmation ou non
lastJsonRecv = {"type": "none"}
socket = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

def sendQuestion(question, socket):
    msg = {"type": "question", "msg": question}
    jsonMsg = json.dumps(msg)
    socket.send(str.encode(jsonMsg))

def sendConfirmation(confirmation, socket):
    msg = {"type": "confirmation", "msg": lastJsonRecv["originalRequest"], "answer": confirmation}
    jsonMsg = json.dumps(msg)
    socket.send(str.encode(jsonMsg))

def askServer(request):
    global socket
    global askConfirmation
    if(request != "") :
        socket = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
        socket.connect((hote, port))

        if not askConfirmation:
            sendQuestion(request, socket)               # Envoi de la première requête
        else:
            sendConfirmation(request, socket)
            askConfirmation = False

        rawRet = socket.recv(1024).decode()
        ret = json.loads(rawRet)
        global lastJsonRecv
        lastJsonRecv = ret

        if (ret["type"] == "askConfirmation"):  # Si le serveur demande des précisions
            printRobot(ret["msg"] + "\n")
            askConfirmation = True
        elif (ret["type"] == "ERROR"):
            printError(ret["msg"])
        else:
            printRobot(ret["msg"])  # Fin de la requête, fermeture socket

        socket.close()


root.mainloop()
