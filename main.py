import random
import time
import json
from pprint import pprint as pp

#from teams import createleague

from game import quickmatchday
from season import main

with open('teams.txt') as f:
    data = json.load(f)

season = main()

#for week in season
for i in season:
    #for match in week
    for i2 in i:
        #for team in match
        match = []
        for i3 in i2:
            match.append(i3)
        quickmatchday(match)
            
            