import socket as sck

hote="localhost"
port = 15555

while True:

    request = input("Ordre : ")
    socket=sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    socket.connect((hote, port))
    print("Connecté à "+hote)
    socket.send(str.encode(request))
    ret = socket.recv(1024).decode()
    print(ret)
    socket.close()
