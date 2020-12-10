import random
import time
import json

with open('teams.txt') as f:
    data = json.load(f)

position = 1

for team in data:
    
    p = str(position) + '. ' + str(team["name"]) + ' ' + str(team["score"])
    print(p)
    position += 1