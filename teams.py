import random
import json

premteams = ['Arsenal', 'Aston Villa', 'Brighton', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Leeds Utd', 'Leicester City', 'Liverpool', 'Manchester Utd', 'Manchester City', 'Newcastle Utd', 'Sheffield Utd', 'Southampton', 'Spurs', 'West Brom', 'West Ham Utd', 'Wolves']


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
    elif name in ["Everton", "Leicester City", "West Ham Utd", "Newcastle Utd", "RB Leipzig", "Sevilla", "Bayer Leverkusen", "Eintracht Frankfurt", "VfL Wolfsburg", "Lyon", "Marseille", "Monaco", "Roma", "Napoli", "Torino"]:
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
        "won": 0,
        "drawn": 0,
        "lost": 0,
        "attack": attnum + bonus,
        "defense": defnum + bonus,
        "luck": lucknum + bonus,
        "speed": speednum + bonus,
        "stamina": stamnum + bonus
    }

    return newteam

dic = {}
key = 1
