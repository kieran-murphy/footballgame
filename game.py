import random
import time
import json
#from teams import createleague

class Team:
    def __init__(self, key, name, score, goaldif, goals, attack, defense, luck, speed, stamina): 
        self.key = key
        self.name = name
        self.score = score
        self.goaldif = goaldif
        self.goals = goals
        self.attack = attack
        self.defense = defense
        self.luck = luck
        self.speed = speed
        self.stamina = stamina
        self.red = False


team1 = Team('Team1', 1, 0, 0, 0, 60, 60, 60, 60, 60)
team2 = Team('Team2', 1, 0, 0, 0, 50, 50, 50, 50, 50)

match = [team1, team2]


def goal(team):
    print("Goal! " + str(team.name) + " scores! ⚽")
    team.score += 1

def yellow(team):
    print("Yellow Card for " + str(team.name) + ' 🟡')

rednum = 50
def red(team):
    if team.red == False:
        print("Red Card for " + str(team.name) + ' 🔴')
        team.red = True
        team.attack -= rednum
        team.defense -= rednum
        team.luck -= rednum
        team.speed -= rednum
        team.stamina -= rednum
    else:
        pass

def quickgoal(team):
    #print("Goal! " + str(team.name) + " scores! ⚽")
    team.goals += 1

def quickred(team):
    if team.red == False:
        #print("Red Card for " + str(team.name) + ' 🔴')
        team.red = True
        team.attack -= rednum
        team.defense -= rednum
        team.luck -= rednum
        team.speed -= rednum
        team.stamina -= rednum
    else:
        pass

def quickprint(team):
    print(team.name + " " + str(team.attack))

def matchday(match):
    for i in range(0, 91):
        if i < 46:
            secondhalf = False
        elif i == 46:
            print('Half Time! ⏱️')
            secondhalf = True
        else:
            secondhalf = True
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
            nVar_1 = random.randint(1,100)
            nVar_2 = random.randint(1,100)
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
            n3_1 = random.randint(1,100)
            n3_2 = random.randint(1,100)
            if secondhalf == True:
                if (match[0].attack + match[0].stamina + n3_1) > (match[1].attack + match[1].stamina + n3_2):
                    goal(match[0])
                else:
                    goal(match[1])
            else:
                if (match[0].attack + match[0].speed + n3_1) > (match[1].attack + match[1].speed + n3_2):
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
    
    print(str(match[0].name) + ' ' + str(match[0].score) + '-' + str(match[1].score) + ' ' + str(match[1].name))
    #print(str(team1.name) + ' ' + str(team1.score) + '-' + str(team2.score) + ' ' + str(team2.name))

def quickmatchday(match, json):
    
    for i in range(0, 91):
        n1 = random.randint(1, 300)
        n2 = random.randint(0,1)
        
        #event = ""
        #nothing happening
        if n1 < 283:
            if match[0].red == True or match[1].red == True:
                pass
            else:
                pass
        #VAR
        elif n1 < 284:
            #print("VAR Decision: Checking Possible Foul! 📺")
            #time.sleep(3)
            nVar = random.randint(0,10)
            nVar_1 = random.randint(1,100)
            nVar_2 = random.randint(1,100)
            if (match[0].luck + nVar_1) > (match[1].luck + nVar_2):
                varteam = match[0]
            else:
                varteam = match[1]
            if nVar > 3:
                #print("Penalty given for " + str(varteam.name) + "!")
                nVar_3 = random.randint(0,4)
                if nVar_3 > 1:
                    quickgoal(varteam)
                else:
                    pass
            else:
                pass

        #goal
        elif n1 < 295:
            #generate new random number here for each team (plus stats) to compare
            n3_1 = random.randint(1,100)
            n3_2 = random.randint(1,100)
            if (match[0].attack + n3_1) > (match[1].attack + n3_2):
                quickgoal(match[0])
            else:
                quickgoal(match[1])
        #yellow card
        elif n1 < 299:
            pass
        #red card 
        else:
            quickred(match[n2])
    for team in match:
        for i in json:
            if i == team.name:
                json[i]["goals"] += team.goals 
    winner = ""
    draw = False
    if match[0].goals > match[1].goals:
        winner = match[0].name
    elif match[0].goals < match[1].goals:
        winner = match[1].name
    else:
        draw = True

    print(str(match[0].name) + ' ' + str(match[0].goals) + '-' + str(match[1].goals) + ' ' + str(match[1].name))

    if draw == True:
#        print('draw')
        for i in json:
            for team in match:
                if i == team.name:
                    
                    json[i]["score"] += 1
    else:
        for i in json:
            if i == winner:
                json[i]["score"] += 3
#                print('winner: ' + winner)
                #elif i == draw:
                #    json[i]["score"] += 3

    #quickprint(match[0])
    return json
#matchday(match)
#quickmatchday(match)