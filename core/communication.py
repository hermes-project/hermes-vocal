import json

def sendAnswer(answer, client):
    msg = { "type": "answer", "msg": answer }
    jsonMsg = json.dumps(msg)
    client.send(str.encode(jsonMsg))


def askConfirmation(confirmMessage, client):
    msg = {"type": "askConfirmation", "msg": confirmMessage}
    jsonMsg = json.dumps(msg)
    client.send(str.encode(jsonMsg))

def recvFromClient(client):
    rawOrder = client.recv(1024).decode('utf-8')
    return json.loads(rawOrder)
