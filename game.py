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


team1 = Team('Team1', 0, 50, 50, 50, 50, 50)
team2 = Team('Team2', 0, 30, 20, 20, 20, 20)

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
        #nothing happening
        if n1 < 283:
            if match[0].red == True or match[1].red == True:
                event = " "
            else:
                event = " "
        #VAR
        elif n1 < 284:
            print("VAR Decision: Checking Possible Foul! 📺")
            time.sleep(3)
            nVar = random.randint(0,10)
            nVar_1 = random.randint(1,50)
            nVar_2 = random.randint(1,50)
            if (match[0].luck + nVar_1) > (match[1].luck + nVar_2):
                varteam = match[0]
            else:
                varteam = match[1]
            if nVar > 3:
                print("Penalty given for " + str(varteam.name) + "!")
                nVar_3 = random.randint(0,4)
                if nVar_3 > 1:
                    goal(varteam)
                else:
                    print("Penalty Missed! ❌")
            else:
                print("No Penalty Given! ❌")

        #goal
        elif n1 < 295:
            #generate new random number here for each team (plus stats) to compare
            n3_1 = random.randint(1,50)
            n3_2 = random.randint(1,50)
            if (match[0].attack + n3_1) > (match[1].attack + n3_2):
                goal(match[0])
            else:
                goal(match[1])
        #yellow card
        elif n1 < 299:
            yellow(match[n2])
        #red card 
        else:
            red(match[n2])
        time.sleep(0.2)
        print(str(i) + """' """ + event)
    print(str(team1.name) + ' ' + str(team1.score) + '-' + str(team2.score) + ' ' + str(team2.name))

matchday(match)

