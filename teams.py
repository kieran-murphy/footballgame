import random

names = ['Applefarm', 'Remote', 'Robot', 'Daggertooth', 'Dynasty', 'Riverdale', 'Hurricane', 'Woodworth', 'Swan', 'Flameport', 'Magnolia', 'Holiday', 'Jolly', 'Sportsball', 'Red Bull', 'Explorer', 'Wolverine', 'Firecracker', 'Ricochet', 'Micro', 'Sturdy', 'Hit or Miss', 'Volcano', 'Bayside', 'Milano', 'Southside', 'Lakeside', 'Dummy', 'Orange', 'Turtle', 'Block', 'August', 'Summer', 'Icy', 'Lightning', 'Pandora', 'Alpha', 'Omega', 'Munchkin', 'Red', 'Pond', 'Cobblestone', 'Snowpass', 'Arrow', 'Auto']
suffixes = ['Albion', 'Wednesday', 'Town', 'Boys', 'Rovers', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC', 'Utd', 'City', 'FC']

newnames = []

while len(newnames) < 13:
    n1 = random.randint(1,len(names)) - 1
    
    nomp = names[n1]
    if nomp not in newnames:
        newnames.append(nomp)
        

for name in newnames:
    n2 = random.randint(1,len(suffixes)) - 1
    name += ' ' + str(suffixes[n2])
    print(name)
    

