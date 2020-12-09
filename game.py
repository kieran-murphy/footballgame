import random
import time

class Team:
    def __init__(self, name, score): 
        self.name = name
        self.score = score

team1 = Team('Man city', 0)
team2 = Team('Tottenham', 0)

def goal(t):
    print("Goal! " + str(t.name) + " scores!")
    t.score += 1

def yellow(t):
    print("Yellow Card for " + str(t.name))

def red(t):
    print("Red Card for " + str(t.name))

for i in range(0, 91):
    n1 = random.randint(1, 300)
    event = ""
    if n1 < 282:
        event = " "
    elif n1 < 294:
        #event = "Goal!"
        goal(team1)
    elif n1 < 299:
        #event = "Yellow Card!"
        yellow(team1)
    else:
        #event = "Red Card!"
        red(team1)
    time.sleep(0.2)
    print(str(i) + """' """ + event)

