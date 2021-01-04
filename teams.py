import random
import json

names = ['Applefarm', 'Daggertooth', 'Dynasty', 'Riverdale', 'Hurricane', 'Woodworth', 'Swan', 'Flameport', 'Magnolia', 'Sportsball', 'Red Bull', 'Explorer', 'Wolverine', 'Firecracker', 'Ricochet', 'Hit or Miss', 'Volcano', 'Bayside', 'Milano', 'Southside', 'Lakeside', 'Orange', 'Turtle', 'Block', 'August', 'Summer', 'Icy', 'Lightning', 'Pandora', 'Alpha', 'Omega', 'Munchkin', 'Red', 'Pond', 'Cobblestone', 'Snowpass', 'Arrow', 'Auto']
suffixes = ['Albion', 'Wednesday', 'Town', 'Boys', 'Rovers', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC', 'FC', 'Utd', 'City', 'FC']

newnames1 = []
newnames2 = [] 

premteams = ['Arsenal', 'Aston Villa', 'Brighton', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Leeds Utd', 'Leicester City', 'Liverpool', 'Manchester Utd', 'Manchester City', 'Newcastle Utd', 'Sheffield Utd', 'Southampton', 'Spurs', 'West Brom', 'West Ham Utd', 'Wolves']

def createnames(names,suffixes):
    
    while len(newnames1) < 20:
        n1 = random.randint(1,len(names)) - 1
    
        nomp = names[n1]
        if nomp not in newnames1:
            newnames1.append(nomp)
        
    for name in newnames1:
        n2 = random.randint(1,len(suffixes)) - 1
        name += ' ' + str(suffixes[n2])
        newnames2.append(name)
        
        
    
    return newnames2

createnames(names,suffixes)
        

def createteam(name, key):
    statsnum = 250
    attnum = random.randint(1,100)
    statsnum -= attnum
    defnum = random.randint(1,100)
    statsnum -= defnum
    lucknum = random.randint(1,50)
    statsnum -= lucknum
    speednum = random.randint(1,statsnum)
    statsnum -= speednum
    stamnum = statsnum
    bonus = 20


    newteam = {
        "key": key,
        "name": name,
        "score": 0,
        "goaldif": 0,
        "goals": 0,
        "attack": attnum + bonus,
        "defense": defnum + bonus,
        "luck": lucknum + bonus,
        "speed": speednum + bonus,
        "stamina": stamnum + bonus
    }

    return newteam
    
def createpremteam(name, key):
    
    attnum = random.randint(70,100)
    
    defnum = random.randint(70,100)
    
    lucknum = random.randint(70,100)
    
    speednum = random.randint(70,100)
    
    stamnum = random.randint(70,100)
    bonus = 0

    tier = 0
    if name in ["Arsenal", "Chelsea", "Manchester Utd", "Manchester City", "Liverpool", "Spurs", "Atlético de Madrid", "Barcelona", "Real Madrid", "Borussia Dortmund", "Bayern Munich", "Paris Saint-Germain", "Inter Milan", "Juventus", "AC Milan"]:
        tier += 1
    elif name in ["Everton", "Wolves", "Leicester City", "West Ham Utd", "Newcastle Utd", "RB Leipzig", "Sevilla", "Bayer Leverkusen", "Eintracht Frankfurt", "VfL Wolfsburg", "Lyon", "Marseille", "Monaco", "Roma", "Napoli", "Torino"]:
        tier += 2
    else:
        tier += 3
    
    if tier == 1:
        bonus += 60
    elif tier == 2:
        bonus += 40
    elif tier == 3:
        bonus += 30

    newteam = {
        "key": key,
        "name": name,
        "score": 0,
        "goaldif": 0,
        "goals": 0,
        "attack": attnum + bonus,
        "defense": defnum + bonus,
        "luck": lucknum + bonus,
        "speed": speednum + bonus,
        "stamina": stamnum + bonus
    }

    return newteam

dic = {}
key = 1
#for name in newnames2:
"""
for name in premteams:
    print(name)
    dic[name] = createpremteam(name, key)
    key += 1
    
with open('teams.txt', 'w') as json_file:
        json.dump(dic, json_file, indent=4)
"""