import random
import json

names = ['Applefarm', 'Daggertooth', 'Dynasty', 'Riverdale', 'Hurricane', 'Woodworth', 'Swan', 'Flameport', 'Magnolia', 'Sportsball', 'Red Bull', 'Explorer', 'Wolverine', 'Firecracker', 'Ricochet', 'Hit or Miss', 'Volcano', 'Bayside', 'Milano', 'Southside', 'Lakeside', 'Orange', 'Turtle', 'Block', 'August', 'Summer', 'Icy', 'Lightning', 'Pandora', 'Alpha', 'Omega', 'Munchkin', 'Red', 'Pond', 'Cobblestone', 'Snowpass', 'Arrow', 'Auto']
suffixes = ['Albion', 'Wednesday', 'Town', 'Boys', 'Rovers', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC', 'FC', 'Utd', 'City', 'FC']

newnames1 = []
newnames2 = []


def createnames(names,suffixes):
    
    while len(newnames1) < 13:
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
    
    newteam = {
        "name": name,
        "score": random.randint(1,10) * 3,
        "attack": random.randint(1,40),
        "defense": random.randint(1,40),
        "luck": random.randint(1,40),
        "speed": random.randint(1,40),
        "stamina": random.randint(1,40)
    }

    return newteam
    
    


array = []
for name in newnames2:
    
    array.append(createteam(name))
    
with open('teams.txt', 'w') as json_file:
        json.dump(array, json_file)





    


    




