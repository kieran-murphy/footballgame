import random
import time
import json
import rich

from rich.console import Console
from rich.table import Table
from pprint import pprint as pp

console = Console()


premteams = ['Arsenal', 'Aston Villa', 'Brighton', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Leeds Utd', 'Leicester City', 'Liverpool', 'Manchester Utd', 'Manchester City', 'Newcastle Utd', 'Sheffield Utd', 'Southampton', 'Spurs', 'West Brom', 'West Ham Utd', 'Wolves']
laligateams = ['Alavés', 'Athletic Bilbao', 'Atlético de Madrid', 'Barcelona', 'Cádiz', 'Celta Vigo', 'Eibar', 'Elche', 'Getafe', 'Granada', 'Huesca', 'Levante', 'Osasuna', 'Real Betis', 'Real Madrid', 'Real Sociedad', 'Sevilla', 'Valencia', 'Valladolid', 'Villarreal']
bundesligateams = ['FC Augsburg', 'Hertha BSC', 'Union Berlin', 'Arminia Bielefeld', 'Werder Bremen', 'Borussia Dortmund', 'Eintracht Frankfurt', 'SC Freiburg', '1899 Hoffenheim', 'FC Köln', 'RB Leipzig', 'Bayer Leverkusen', 'Mainz 05', 'Borussia Mönchengladbach', 'Bayern Munich', 'Schalke 04', 'VfB Stuttgart', 'VfL Wolfsburg', 'Hannover 96', 'Hamburger SV']
ligue1teams = ['Angers', 'Bordeaux', 'Brest', 'Dijon', 'Lens', 'Lille', 'Lorient', 'Lyon', 'Marseille', 'Metz', 'Monaco', 'Montpellier', 'Nantes', 'Nice', 'Nîmes', 'Paris Saint-Germain', 'Reims', 'Rennes', 'Saint-Étienne', 'Strasbourg']
serieateams = ['Atalanta', 'Benevento', 'Bologna', 'Cagliari', 'Crotone', 'Fiorentina', 'Genoa', 'Hellas Verona', 'Inter Milan', 'Juventus', 'Lazio', 'AC Milan', 'Napoli', 'Parma', 'Roma', 'Sampdoria', 'Sassuolo', 'Spezia', 'Torino', 'Udinese']

#dic is used to dump team data into and then write into JSON
dic = {}
#key is a unique primary key for each team and used to select 1-20
key = 1

from game import quickmatchday, matchday, Team
from teams import createpremteam


print("1. Premier League")
print("2. La Liga")
print("3. Bundesliga")
print("4. Ligue 1")
print("5. Serie A")
print("")

leaguechoicecorrect = False
leaguecolor = ""
teamcolor = ""

while leaguechoicecorrect == False:
    leaguechoice = input("Choose a league: ")

    
    if leaguechoice == "1":
        leaguechoicecorrect = True
        for name in premteams:
            dic[name] = createpremteam(name, key)
            leaguecolor = "bright_magenta"
            teamcolor = "turquoise2 bold italic"
            key += 1
    elif leaguechoice == "2":
        leaguechoicecorrect = True
        for name in laligateams:
            dic[name] = createpremteam(name, key)
            leaguecolor = "orange1"
            teamcolor = "sandy_brown bold italic"
            key += 1
    elif leaguechoice == "3":
        leaguechoicecorrect = True
        for name in bundesligateams:
            dic[name] = createpremteam(name, key)
            leaguecolor = "yellow1"
            teamcolor = "wheat1 bold italic"
            key += 1
    elif leaguechoice == "4":
        leaguechoicecorrect = True
        for name in ligue1teams:
            dic[name] = createpremteam(name, key)
            leaguecolor = "red3"
            teamcolor = "blue bold italic"
            key += 1
    elif leaguechoice == "5":
        leaguechoicecorrect = True
        for name in serieateams:
            dic[name] = createpremteam(name, key)
            leaguecolor = "chartreuse3"
            teamcolor = "dark_olive_green3 bold italic"
            key += 1
    else:
        print("Wrong choice! Please pick a number between 1 and 5")



with open('teams.txt', 'w') as json_file:
        json.dump(dic, json_file, indent=4)

#opens the json file with team data
with open('teams.txt') as f:
    data = json.load(f)

from rank import statrank, seasonrank, findhigheststat
from ladder import createladder
from richladder import createrichladder
from season import make_season

#creates the season's fixture list
season = make_season()

#reset the score and goals for each season
for i in data:
        data[i]['score'] = 0
        data[i]['goals'] = 0

#used to print the gameweek string
gameweeknum = 0
#used to determine the next gameweek index, i.e. your next opponent is list[futurenum]
futurenum = 0

#choosing a team using number input
print('Choose a team to play: \n ')
createladder(data)
numinputchoices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
numinputcorrect = False
while numinputcorrect == False:
    numinput = input('Choose a team number: ')
    if numinput in numinputchoices:
        numinputcorrect = True
        userteamkey = int(numinput)
    else:
        print("Wrong choice! Please pick a number between 1 and 20")
#match key to input and then ask to change name

seasonlength = 38            

#userbonus is given to make the teams in tier 2
userbonus = 40
if userteamkey < 21:
    if userteamkey > 0:
        #g = team as a class, easier and quicker to write
        for g in data:
            #checks the team selected is valid
            if userteamkey == data[g]['key']:
                userteam = data[g]['name']
                
                with open('teams.txt', 'w') as json_file:
                    json.dump(data, json_file, indent=4)
                #chosing stats for the team    
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
                    #used to print gameweeks
                    gameweeknum += 1
                    #used to determine next opponent by skipping ahead by 1 in the index
                    upcomingArray = []
                    x = 0 
                    for i in season:
                        upcomingArray.append(i)
                        x += 1
                    
                    if futurenum > 36:
                        pass
                    else:
                        for j in upcomingArray[futurenum]:
                            if j[0] == data[g]['name']:
                                print('Your next opponent is ' + j[1])
                            elif j[1] == data[g]['name']:
                                print('Your next opponent is ' + j[0])
                    #asks the user their choice of whether they want to play or skip the next game
                    print("1. Play")
                    print("2. Skip")
                    gamechoice = input("Would you like to play this game or skip? ")
                    print(" ")
                    print('Gameweek: ' + str(gameweeknum))
                    print(" ")

                    #newweek is created to ensure that the user team is always at the front of the gameweek for readability
                    newweek = []
                    for matchbrackets in week:
                        newweek.append(matchbrackets)
                        for m in newweek:
                            if userteam in m:
                                newweek.remove(m)
                                newweek.insert(0, m)

                    #for each match in a week, set up the game using temporary versions of the team class
                    for matchbrackets in newweek:
                        match0 = []
                        match1 = [] 
                        for team in matchbrackets:
                            match0.append(team)
                        team1 = Team(0, str(match0[0]), 0, 0, 0, 0, 0, 0, data[match0[0]]['attack'], data[match0[0]]['defense'], data[match0[0]]['luck'], data[match0[0]]['speed'], data[match0[0]]['stamina'])
                        team2 = Team(0, str(match0[1]), 0, 0, 0, 0, 0, 0, data[match0[1]]['attack'], data[match0[1]]['defense'], data[match0[1]]['luck'], data[match0[1]]['speed'], data[match0[1]]['stamina'])
                        match1.append(team1)
                        match1.append(team2)
                         
                        
                        
                        if userteam in match0:
                            #if user wants to play a game use long game mode matchday
                            if gamechoice == "1":    
                                print(match0[0] + " vs " + match0[1])
                                print(' ')
                                matchday(match1, data)
                                print(' ')
                                print('Gameweek: ' + str(gameweeknum))
                                print(' ')
                            
                            else:
                                quickmatchday(match1, data)
                        else:
                            quickmatchday(match1, data)

                        with open('teams.txt', 'w') as json_file:
                            json.dump(data, json_file, indent=4)
                        
                    print(' ')
                    createrichladder(data, leaguecolor, teamcolor, data[g]['name'], gameweeknum)
                    print(' ')

                    #adds to futurenum so the future fixture can be seen accurately as it was read before
                    futurenum += 1
                    if futurenum > 36:
                        pass
                    else:
                        for j in upcomingArray[futurenum]:
                            
                            if j[0] == data[g]['name']:
                                print('Your next opponent is ' + j[1] + " they are " + findhigheststat(data, j[1]) + " team.")
                            elif j[1] == data[g]['name']:
                                print('Your next opponent is ' + j[0] + " they are " + findhigheststat(data, j[0]) + " team.")
                            
                    #if before gameweek 38 (last one), give the user the choice of upgrading one of 5 stats by a random 0-6 amount each week in "training"
                    statchoices1 = ["attack", "defense", "luck", "speed", "stamina"]
                    statchoices2 = []

                    if futurenum > 37:
                        pass
                    else:
                        for i in range(0,3):
                            #takes away from statchoices1 to add to statchoices2 for user selection
                            statchoices2.append(statchoices1.pop(random.randint(0, len(statchoices1) - 1)))
                        num = 1
                        for i in statchoices2:
                            #prints capital version of the stats, need to be lowercase so they work in the JSON and with the class structure
                            print(str(num) + ". " + i.capitalize())
                            num += 1
                        

                        upgradechoice = input("Choose a stat to train: ")
                        if upgradechoice == "1" or upgradechoice == "2" or upgradechoice == "3":
                            stattoupgrade = statchoices2[int(upgradechoice) - 1]
                        else:
                            #if an invalid number is chosen, pick a random one
                            upgradechoice = random.randint(0,2)
                            print('Invalid choice: random chosen')
                            print(' ')
                            stattoupgrade = statchoices2[upgradechoice - 1]
                        #amount of upgrade will be randomly selected between 0-6
                        upgradeamount = random.randint(0,6)
                        #adds on upgrade
                        data[g][stattoupgrade] += upgradeamount
                        #prints how much a stat has been upgraded by and what rank that team sits at in that specific rank
                        print(stattoupgrade.capitalize() + (' upgraded by ' + str(upgradeamount) + '! ' + statrank(data, stattoupgrade, data[g]['name'])))

                        #makes the user press enter before moving onto the next week
                        next = input('Press Enter for next gameweek')
                        print(' ')    
                    
                #prints at the end of a season where the team finished, and if they won, qualified for a european competition or got relegated
                print(' ')    
                seasonrank(data, data[g]['name'])
                print(' ')

    else:
        print('invalid input')
else:
    print('invalid input')