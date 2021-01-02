import random
import time
import json


with open('teams.txt') as f:
    data = json.load(f)

attack = "speed"
userteam = "Brighton"

def statrank(data, stat, userteam):

    dicc = {}

    for team in data:
        dicc[team] = data[team][stat]

    sorteddicc = sorted(dicc, key=dicc.get, reverse=True)
    
    teampos = 0
    position = 1
    for equipo in sorteddicc:
        if equipo == userteam:
            teampos = position
        #p = str(position) + '. ' + equipo + ' ' + str(dicc[equipo])
        #print(p)
        position += 1
    if teampos == 1:
        teampos = str(teampos) + "st"
    elif teampos == 2:
        teampos = str(teampos) + "nd"
    else:
        teampos = str(teampos) + "th"
    statement = ('You are ' + teampos + " in " + str(stat) + "!")
    return(statement)

def seasonrank(data, userteam):

    dicc = {}

    for team in data:
        dicc[team] = data[team]['score']

    sorteddicc = sorted(dicc, key=dicc.get, reverse=True)
    
    teampos = 0
    position = 1
    for equipo in sorteddicc:
        if equipo == userteam:
            teampos = position
        #p = str(position) + '. ' + equipo + ' ' + str(dicc[equipo])
        #print(p)
        position += 1
    if teampos == 1:
        teampos = str(teampos) + "st"
    elif teampos == 2:
        teampos = str(teampos) + "nd"
    else:
        teampos = str(teampos) + "th"
    statement = ('You finished ' + teampos + "!")
    return(statement)

def findhigheststat(data, team):
    stats = ["attack", "defense", "luck", "speed", "stamina"]
    higheststat = ""
    statforreturn = ""
    higheststatnum = 0
    for stat in stats:
        if int(data[team][stat]) > higheststatnum:
            higheststat = stat
            print(higheststat)
        #print(stat, data[team][stat])
    
    if higheststat == "attack":
        statforreturn = "an attacking"
    elif higheststat == "defense":
        statforreturn = "a defensive"
    elif higheststat == "luck":
        statforreturn = "a lucky"
    elif higheststat == "speed":
      statforreturn = "a speedy"
    elif higheststat == "stamina":
        statforreturn = "a fit"
    
    return statforreturn

#print(statrank(data, attack, userteam))

print(findhigheststat(data, userteam))