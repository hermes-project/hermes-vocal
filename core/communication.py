import json
from core.utils.cleanString import cleanString

yesWords = ["oui", "d'accord", "d accord", "ok", "ça marche", "pourquoi pas", "bien sur"]
noWords = ["non", "pas du tout", "hors de question", "pas question", "impossible", "je refuse"]

def sendAnswer(answer, client):
    msg = { "type": "answer", "msg": answer }
    jsonMsg = json.dumps(msg)
    client.send(str.encode(jsonMsg))


def askConfirmation(confirmMessage, client):
    msg = {"type": "askConfirmation", "msg": confirmMessage}
    jsonMsg = json.dumps(msg)
    client.send(str.encode(jsonMsg))
    conf = recvFromClient(client)
    if conf["type"] == "confirmation":
        for word in noWords:
            if word in cleanString(conf["msg"]):
                return False
        for word in yesWords:
            if word in cleanString(conf["msg"]):
                return True
        return False
    #TODO: renvoyer l'ordre normal dans le core
    return False # en attendant


def recvFromClient(client):
    rawOrder = client.recv(1024).decode('utf-8')
    return json.loads(rawOrder)
