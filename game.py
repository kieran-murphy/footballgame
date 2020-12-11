import random
import time
import json
#from teams import createleague

class Team:
    def __init__(self, name, score, attack, defense, luck, speed, stamina): 
        self.name = name
        self.score = score
        self.attack = attack
        self.defense = defense
        self.luck = luck
        self.speed = speed
        self.stamina = stamina
        self.red = False


team1 = Team('Hit or Miss', 0, 50, 50, 50, 50, 50)
team2 = Team('Yeah the Mooys', 0, 10, 10, 10, 10, 10)

match = [team1, team2]

def goal(team):
    print("Goal! " + str(team.name) + " scores! ⚽")
    team.score += 1

def yellow(team):
    print("Yellow Card for " + str(team.name) + ' 🟡')

def red(team):
    if team.red == False:
        print("Red Card for " + str(team.name) + ' 🔴')
        team.red = True
    else:
        pass

def matchday(match):
    for i in range(0, 91):
        n1 = random.randint(1, 300)
        n2 = random.randint(0,1)
        event = ""
        if n1 < 282:
            if match[0].red == True or match[1].red == True:
                event = " "
            else:
                event = " "
        elif n1 < 294:
            goal(match[n2])
        elif n1 < 299:
            yellow(match[n2])
        else:
            red(match[n2])
        time.sleep(0.2)
        print(str(i) + """' """ + event)
    print(str(team1.name) + ' ' + str(team1.score) + '-' + str(team2.score) + ' ' + str(team2.name))

matchday(match)

