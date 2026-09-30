import json
from .player import p

def saveData():
    data = {
    "Player": p.name,
    "Age": p.age,
    "Items": p.inventory,
    }

    with open("save.json", "w") as saveFile:
        json.dump(vars(data), saveFile)

def loadData():
    with open("save.json", "r") as saveFile:
        loadData = json.load(saveFile)
    return loadData