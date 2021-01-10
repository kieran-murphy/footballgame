import random
import time
import json


with open('teams.txt') as f:
    data = json.load(f)

#with a stat and a team as an argument, find out how good a team is at a stat, i.e. arsenal is 4th in speed
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
        
        position += 1
    if teampos == 1:
        teampos = str(teampos) + "st"
    elif teampos == 2:
        teampos = str(teampos) + "nd"
    elif teampos == 3:
        teampos = str(teampos) + "rd"
    else:
        teampos = str(teampos) + "th"
    statement = ('You are ' + teampos + " in " + str(stat) + "!")
    return(statement)

#at the end of a season, find a teams position and give text based on if they get relegated or win etc.
def seasonrank(data, userteam):

    dicc = {}

    for team in data:
        dicc[team] = data[team]['score']

    sorteddicc = sorted(dicc, key=dicc.get, reverse=True)
    
    teampos = 0
    position = 1
    suffix = " "
    for equipo in sorteddicc:
        if equipo == userteam:
            teampos = position
        
        position += 1
    if teampos == 1:
        teampos = str(teampos) + "st"
        suffix = "You won the league! 🏆 👏 🥳 "
    elif teampos == 2:
        teampos = str(teampos) + "nd"
        suffix = "You qualified for the Champions league! "
    elif teampos == 3:
        teampos = str(teampos) + "rd"
        suffix = "You qualified for the Champions league! "
    elif teampos == 4:
        teampos = str(teampos) + "th"
        suffix = "You qualified for the Champions league! "
    elif teampos < 7:
        teampos = str(teampos) + "th"
        suffix = "You qualified for the Europa league! "
    elif teampos > 17:
        teampos = str(teampos) + "th"
        suffix = "You got relegated... 😢 ⬇️ "
    else:
        teampos = str(teampos) + "th"

    statement = ('You finished ' + teampos + "!")
    print(statement)
    print(suffix)


# find the highest stat for a team, i.e. leeds utd are an attacking team
def findhigheststat(data, team):
    stats = ["attack", "defense", "luck", "speed", "stamina"]
    higheststat = ""
    statforreturn = ""
    higheststatnum = 0
    for stat in stats:
        if data[team][stat] > higheststatnum:
            higheststatnum = data[team][stat]
            higheststat = stat
            
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


