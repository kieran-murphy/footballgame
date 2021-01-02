import random
import time
import json
import rich
from pprint import pprint as pp


#each 3 weeks
#what would you like to train today?
#give 3 random stats
#randomint 1-5 increase

premteams = ['Arsenal', 'Aston Villa', 'Brighton', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Leeds Utd', 'Leicester City', 'Liverpool', 'Manchester Utd', 'Manchester City', 'Newcastle Utd', 'Sheffield Utd', 'Southampton', 'Spurs', 'West Brom', 'West Ham Utd', 'Wolves']
dic = {}
key = 1
#for name in newnames2:
from game import quickmatchday, Team

from teams import createpremteam

for name in premteams:
    #print(name)
    dic[name] = createpremteam(name, key)
    key += 1

with open('teams.txt', 'w') as json_file:
        json.dump(dic, json_file, indent=4)

#makes the seasons fixtures
with open('teams.txt') as f:
    data = json.load(f)

from rank import statrank, seasonrank, findhigheststat
from ladder import createladder
from season import make_season

season = make_season()

#reset the score and goals for each season
for i in data:
        data[i]['score'] = 0
        data[i]['goals'] = 0

#for week in season
num = 0
x1 = 0


print('Choose a team to play: \n ')
createladder(data)
numinput = input('Choose a team number: ')
userteamkey = int(numinput)
#match key to input and then ask to change name

userbonus = 40
if userteamkey < 21:
    if userteamkey > 0:
        for g in data:
            if userteamkey == data[g]['key']:
                
                #data[g]['name'] = "~" + data[g]['name'] + "~"
                with open('teams.txt', 'w') as json_file:
                    json.dump(data, json_file, indent=4)
                print('You have chosen: ' + data[g]['name'])
                input('Press Enter for Attack: ')
                rollattack = random.randint(70,100) + userbonus
                data[g]['attack'] = rollattack
                print('You got ' + str(rollattack) + '! ' + statrank(data, 'attack', data[g]['name']))

                input('Press Enter for Defense: ')
                rolldefense = random.randint(70,100) + userbonus
                data[g]['defense'] = rolldefense
                print('You got ' + str(rolldefense) + '! ' + statrank(data, 'defense', data[g]['name']))

                input('Press Enter for Luck: ')
                rollluck = random.randint(70,100) + userbonus
                data[g]['luck'] = rollluck
                print('You got ' + str(rollluck) + '! ' + statrank(data, 'luck', data[g]['name']))

                input('Press Enter for Speed: ')
                rollspeed = random.randint(70,100) + userbonus
                data[g]['speed'] = rollspeed
                print('You got ' + str(rollspeed) + '! ' + statrank(data, 'speed', data[g]['name']))

                input('Press Enter for Stamina: ')
                rollstamina = random.randint(70,100) + userbonus
                data[g]['stamina'] = rollstamina
                print('You got ' + str(rollstamina) + '! ' + statrank(data, 'stamina', data[g]['name']))

                input('Press Enter to start season! ')

                with open('teams.txt', 'w') as json_file:
                    json.dump(data, json_file, indent=4)


                for week in season:
                    num += 1
                    print(' ')
                    print('Gameweek: ' + str(num))
                    for matchbrackets in week:
                        #for team in match
                        match0 = []
                        match1 = [] 
                        for team in matchbrackets:
                            match0.append(team)
                        team1 = Team(0, str(match0[0]), 0, 0, 0, data[match0[0]]['attack'], data[match0[0]]['defense'], data[match0[0]]['luck'], data[match0[0]]['speed'], data[match0[0]]['stamina'])
                        team2 = Team(0, str(match0[1]), 0, 0, 0, data[match0[1]]['attack'], data[match0[1]]['defense'], data[match0[1]]['luck'], data[match0[1]]['speed'], data[match0[1]]['stamina'])
                        match1.append(team1)
                        match1.append(team2)
                        quickmatchday(match1, data)

                        with open('teams.txt', 'w') as json_file:
                            json.dump(data, json_file, indent=4)
                    print(' ')
                    createladder(data)
                    print(' ')
                    
                    
                    #shows the upcoming games 
                    
                    """
                    upcomingArray = []
                    x = 0 
                    for i in season:
                        if x == 0:
                            pass
                        else:
                            upcomingArray.append(i)
                        x += 1

                    if x1 >= 37:
                        pass
                    else:
                        print('Upcoming: ')
                        for j in upcomingArray[x1]:
                            
                            print(str(j[0]) + ' ' + '-' + ' ' + str(j[1]))
                    """
                    
                    upcomingArray = []
                    x = 0 
                    for i in season:
                        if x == 0:
                            pass
                        else:
                            upcomingArray.append(i)
                        x += 1

                    if x1 >= 37:
                        pass
                    else:
                        #print('Upcoming: ')
                        for j in upcomingArray[x1]:
                            
                            
                            if j[0] == data[g]['name']:
                                print('Your next opponent is ' + j[1] + " they are " + findhigheststat(data, j[1]) + " team.")
                            elif j[1] == data[g]['name']:
                                print('Your next opponent is ' + j[0] + " they are " + findhigheststat(data, j[0]) + " team.")
                            #print(str(j[0]) + ' ' + '-' + ' ' + str(j[1]))

                    statchoices0 = ["attack", "defense", "luck", "speed", "stamina"]
                    statchoices1 = ["attack", "defense", "luck", "speed", "stamina"]
                    statchoices2 = []
                    for i in range(0,3):
                        statchoices2.append(statchoices1.pop(random.randint(0, len(statchoices1) - 1)))
                    num = 1
                    for i in statchoices2:
                        print(str(num) + ". " + i.capitalize())
                        num += 1
                    upgradechoice = int(input("Choose a stat to train: "))
                    stattoupgrade = statchoices2[upgradechoice - 1]
                    upgradeamount = random.randint(1,5)

                    data[g][stattoupgrade] += upgradeamount
                    print(stattoupgrade.capitalize() + (' upgraded by ' + str(upgradeamount) + '! ' + statrank(data, stattoupgrade, data[g]['name'])))

                    
                    
                    next = input('Press Enter for next gameweek')    
                    
                    x1 += 1
                    
                print(seasonrank(data, data[g]['name']))

    else:
        print('invalid input')
else:
    print('invalid input')

            
            