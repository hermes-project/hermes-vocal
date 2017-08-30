# Vocal interface
import socket
import json
from core.utils.logs import *
from core import core
from core.communication import *
import core.utils.client as clientglobal

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))

logHeader("######################")
logHeader("#    VOCAL SERVER    #")
logHeader("######################")

while(42):

    logUnderline("--- Attente de requête ---")

    socket.listen(5)
    clientglobal.client, address = socket.accept()

    logGreen("Client connecté...\n")


    order = recvFromClient(clientglobal.client)

    if (order["type"] == "question" or order["type"] == "confirmation"):
        print("Reçu ordre de type "+order["type"])
    else:
        print ("ORDRE DE TYPE NON RECONNU : "+order)

    print("Request : ")
    logBlue(order["msg"])

    ret = core.executeSkill(order["msg"].lower())

    if(ret!="") :
        logBold("Response : "+ret)
        sendAnswer(ret, clientglobal.client)

    print("Close")
    clientglobal.client.close()

    print("\n--------------\n")

