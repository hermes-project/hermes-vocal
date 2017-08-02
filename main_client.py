import socket as sck
from core.utils.logs import *

#hote="172.16.84.9"
hote="localhost"
port = 15555

while True:

    request = input("Ordre : ")
    socket=sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    socket.connect((hote, port))
    ("Connecté à "+hote)
    socket.send(str.encode(request))
    ret = socket.recv(1024).decode()
    logGreen(ret+"\n")
    socket.close()
    if(request != "") :
        socket=sck.socket(sck.AF_INET, sck.SOCK_STREAM)
        socket.connect((hote, port))
        logBlue("Connecté à "+hote)
        socket.send(str.encode(request))
        ret = socket.recv(1024).decode()
        logGreen(ret)
        socket.close()
