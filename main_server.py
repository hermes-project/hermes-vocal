# Vocal interface
import socket
from core.SpeechAndText import STTTS

from core import core

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))

print("######################")
print("#    VOCAL SERVER    #")
print("######################")

while(42):

    print("--- Attente de requête ---")

    socket.listen(5)
    client, address = socket.accept()
    print("Client connecté...\n")

    order = client.recv(1024).decode()
    print("Request : ")
    print(order)

    ret = core.executeSkill(order)

    print("Response : "+ret)
    client.send(str.encode(ret))

    print("Close")
    client.close()

    print("\n--------------\n")

