# Vocal interface
import socket
import json
from core.utils.logs import *
from core.utils.cleanOrder import *
from core import core
from core.communication import *

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))

logHeader("######################")
logHeader("#    VOCAL SERVER    #")
logHeader("######################")

while(42):

    logUnderline("--- Attente de requête ---")

    socket.listen(5)
    client, address = socket.accept()

    logGreen("Client connecté...\n")


    orderJson = recvFromClient(client)

    if (orderJson["type"] == "question" or orderJson["type"] == "confirmation"):
        print("Reçu ordre de type "+orderJson["type"])
    else:
        print ("ORDRE DE TYPE NON RECONNU : "+orderJson)

    print("Request : ")
    logBlue(orderJson["msg"])

    orderJson["client"] = client
    orderJson = cleanOrder(orderJson)

    ret = core.executeSkill(orderJson) #TODO tout transformer en JSON !!!

    if(ret!="") :
        logBold("Response : "+ret)
        sendAnswer(ret, client)

    print("Close")
    client.close()

    print("\n--------------\n")

