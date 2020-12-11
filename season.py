import random
import time
import json

with open('teams.txt') as f:
    data = json.load(f)
season1 = []
season2 = []
season3 = []

for team in data:
    season1.append(team["name"])
    season2.append(team["name"])

for team in season1:
    for team2 in season2:
        if team != team2:
            print(team + " vs " + team2)