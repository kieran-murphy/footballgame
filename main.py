import random
import time
import json
from pprint import pprint as pp

#from teams import createleague

from game import quickmatchday, Team
from season import main

with open('teams.txt') as f:
    data = json.load(f)

season = main()

for i in data:
        data[i]['score'] = 0
        data[i]['goals'] = 0

#for week in season
num = 0
for week in season:
    #for match in week
    num += 1
    print(' ')
    print('Gameweek: ' + str(num))
    for matchbrackets in week:
        #for team in match
        match0 = []
        match1 = [] 
        for team in matchbrackets:
            match0.append(team)
        team1 = Team(str(match0[0]), 0, 0, 0, 80, 80, 80, 80, 80)
        team2 = Team(str(match0[1]), 0, 0, 0, 80, 80, 80, 80, 80)
        match1.append(team1)
        match1.append(team2)
        quickmatchday(match1, data)

with open('teams.txt', 'w') as json_file:
        json.dump(data, json_file)
            
            