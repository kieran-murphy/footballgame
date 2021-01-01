import random
import time
import json
from ladder import createladder
from pprint import pprint as pp

#from teams import createleague

from game import quickmatchday, Team
from season import make_season

with open('teams.txt') as f:
    data = json.load(f)

season = make_season()

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
        team1 = Team(0, str(match0[0]), 0, 0, 0, data[match0[0]]['attack'], data[match0[0]]['defense'], data[match0[0]]['luck'], data[match0[0]]['speed'], data[match0[0]]['stamina'])
        team2 = Team(0, str(match0[1]), 0, 0, 0, data[match0[1]]['attack'], data[match0[1]]['defense'], data[match0[1]]['luck'], data[match0[1]]['speed'], data[match0[1]]['stamina'])
        match1.append(team1)
        match1.append(team2)
        quickmatchday(match1, data)
print(' ')
print(' ')
createladder(data)

with open('teams.txt', 'w') as json_file:
        json.dump(data, json_file, indent=4)
            
            