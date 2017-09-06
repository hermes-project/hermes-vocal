import socket as sck
from core.utils.logs import *
import json

#hote="172.16.84.9"
hote="localhost"
port = 15555

def sendQuestion(question, socket):
    msg = {"type": "question", "msg": question}
    jsonMsg = json.dumps(msg)
    socket.send(str.encode(jsonMsg))



def sendConfirmation(confirmation, socket):
    msg = {"type": "confirmation", "msg": confirmation}
    jsonMsg = json.dumps(msg)
    socket.send(str.encode(jsonMsg))

while True:

    request = input("Ordre : ")

    if(request != "") :

        socket=sck.socket(sck.AF_INET, sck.SOCK_STREAM)
        socket.connect((hote, port))
        logBlue("Connecté à "+hote)
        sendQuestion(request, socket)               # Envoi de la première requête
        #socket.send(str.encode(request))
        rawRet = socket.recv(1024).decode()
        if(rawRet) :
            ret = json.loads(rawRet)
            while(ret["type"]=="askConfirmation"):     # Tant que le serveur demande des précisions
                logGreen(ret["msg"]+"\n")
                resp = input("Réponse : ")
                sendConfirmation(resp, socket)
                rawRet = socket.recv(1024).decode()
                ret = json.loads(rawRet)

            if(ret["type"] == "ERROR") :
                logFail(ret["msg"])
            else :
                logGreen(ret["msg"])                        # Fin de la requête, fermeture socket

            socket.close()
        else :
            logFail("Pas de réponse du serveur")
            socket.close()

