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

#for week in season
for week in season:
    #for match in week
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
            
            