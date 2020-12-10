import random
import time
import json
#rom teams import createleague

names = ['Applefarm', 'Daggertooth', 'Dynasty', 'Riverdale', 'Hurricane', 'Woodworth', 'Swan', 'Flameport', 'Magnolia', 'Sportsball', 'Red Bull', 'Explorer', 'Wolverine', 'Firecracker', 'Ricochet', 'Hit or Miss', 'Volcano', 'Bayside', 'Milano', 'Southside', 'Lakeside', 'Orange', 'Turtle', 'Block', 'August', 'Summer', 'Icy', 'Lightning', 'Pandora', 'Alpha', 'Omega', 'Munchkin', 'Red', 'Pond', 'Cobblestone', 'Snowpass', 'Arrow', 'Auto']
suffixes = ['Albion', 'Wednesday', 'Town', 'Boys', 'Rovers', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC', 'FC', 'Utd', 'City', 'FC']


class Team:
    def __init__(self, name, score, attack, defense, luck, speed, stamina): 
        self.name = name
        self.score = score
        self.attack = attack
        self.defense = defense
        self.luck = luck
        self.speed = speed
        self.stamina = stamina


team1 = Team('Man city', 0, 50, 50, 50, 50, 50)
team2 = Team('Huddersfield', 0, 10, 10, 10, 10, 10)

def goal(t):
    print("Goal! " + str(t.name) + " scores!")
    t.score += 1

def yellow(t):
    print("Yellow Card for " + str(t.name))

def red(t):
    print("Red Card for " + str(t.name))

for i in range(0, 91):
    n1 = random.randint(1, 300)
    n2 = random.randint(0,1)
    a = [team1, team2]
    event = ""
    if n1 < 282:
        event = " "
    elif n1 < 294:
        goal(a[n2])
    elif n1 < 299:
        yellow(a[n2])
    else:
        red(a[n2])
    time.sleep(0.2)
    print(str(i) + """' """ + event)

print(str(team1.name) + ' ' + str(team1.score) + '-' + str(team2.score) + ' ' + str(team2.name))

#createleague(names, suffixes)