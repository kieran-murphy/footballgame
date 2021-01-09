import random
import time
import json


with open('teams.txt') as f:
    data = json.load(f)

def createladder(data):

    dicc = {}

    for team in data:
        dicc[data[team]['name']] = data[team]["score"]

    sorteddicc = sorted(dicc, key=dicc.get, reverse=True)

    position = 1
    for team in sorteddicc:
        p = str(position) + '. ' + team
        print(p)
        position += 1


