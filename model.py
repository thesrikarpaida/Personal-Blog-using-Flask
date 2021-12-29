import json

def loadDb():
    with open("appData.json") as f:
        return json.load(f)

def urlList():
    with open("sites.json") as f:
        return json.load(f)
'''
def contentRead(i):
    # filename = str(i) + ".txt"
    with open(filename) as input_file:
        text = input_file
'''
db = loadDb()
links = urlList()