# Vocal interface
import socket
from core.utils.logs import *
from core import core

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

    order = client.recv(1024).decode().lower()
    print("Request : ")
    logBlue(order)

    ret = core.executeSkill(order)

    logBold("Response : "+ret)
    client.send(str.encode(ret))

    print("Close")
    client.close()

    print("\n--------------\n")

