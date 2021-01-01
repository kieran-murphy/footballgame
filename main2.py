import random
import time
import json
import rich
from pprint import pprint as pp

#from teams import createleague

#roll for each stat
#56 attack! you are ranked 4th in attack

#each 3 weeks
#what would you like to train today?
#give 3 random stats
#randomint 1-5 increase

from game import quickmatchday, Team
from season import make_season
from ladder import createladder


with open('teams.txt') as f:
    data = json.load(f)

#makes the seasons fixtures
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
                
                print('You have chosen: ' + data[g]['name'])
                input('Press Enter for Attack: ')
                rollattack = random.randint(70,100) + userbonus
                data[g]['attack'] = rollattack
                print('You got ' + str(rollattack) + ' attack! 8th highest in the league')

                input('Press Enter for Defense: ')
                rolldefense = random.randint(70,100) + userbonus
                data[g]['defense'] = rolldefense
                print('You got ' + str(rolldefense) + ' defense! 8th highest in the league')

                input('Press Enter for Luck: ')
                rollluck = random.randint(70,100) + userbonus
                data[g]['luck'] = rollluck
                print('You got ' + str(rollluck) + ' luck! 8th highest in the league')

                input('Press Enter for Speed: ')
                rollspeed = random.randint(70,100) + userbonus
                data[g]['speed'] = rollspeed
                print('You got ' + str(rollspeed) + ' speed! 8th highest in the league')

                input('Press Enter for Stamina: ')
                rollstamina = random.randint(70,100) + userbonus
                data[g]['stamina'] = rollstamina
                print('You got ' + str(rollstamina) + ' stamina! 8th highest in the league')

                print(' ')
                print(data[g]['attack'])
                print(data[g]['defense'])
                print(data[g]['luck'])
                print(data[g]['speed'])
                print(data[g]['stamina'])

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
                        next = input('Press Enter for next gameweek')    
                    x1 += 1

    else:
        print('invalid input')
else:
    print('invalid input')



    

        

            



            
            