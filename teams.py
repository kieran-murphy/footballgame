import random
import json

names = ['Applefarm', 'Daggertooth', 'Dynasty', 'Riverdale', 'Hurricane', 'Woodworth', 'Swan', 'Flameport', 'Magnolia', 'Sportsball', 'Red Bull', 'Explorer', 'Wolverine', 'Firecracker', 'Ricochet', 'Hit or Miss', 'Volcano', 'Bayside', 'Milano', 'Southside', 'Lakeside', 'Orange', 'Turtle', 'Block', 'August', 'Summer', 'Icy', 'Lightning', 'Pandora', 'Alpha', 'Omega', 'Munchkin', 'Red', 'Pond', 'Cobblestone', 'Snowpass', 'Arrow', 'Auto']
suffixes = ['Albion', 'Wednesday', 'Town', 'Boys', 'Rovers', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC', 'FC', 'Utd', 'City', 'FC']

newnames1 = []
newnames2 = []


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
        print(name)
        
    
    return newnames2

createnames(names,suffixes)
        

def createteam(name):
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


    newteam = {
        "name": name,
        "score": 0,
        "goaldif": 0,
        "goals": 0,
        "attack": attnum + 20,
        "defense": defnum + 20,
        "luck": lucknum + 20,
        "speed": speednum + 20,
        "stamina": stamnum + 20
    }

    return newteam
    
 

dic = {}
for name in newnames2:
    
    dic[name] = createteam(name)
    
with open('teams.txt', 'w') as json_file:
        json.dump(dic, json_file)
