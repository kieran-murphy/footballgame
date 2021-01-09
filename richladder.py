from rich.console import Console
from rich.table import Table
from rich import inspect

import random
import time
import json

with open('teams.txt') as f:
    data = json.load(f)


def createrichladder(data, leaguecolor, teamcolor, userteam, gameweek):
    
    table = Table(show_header=True, header_style=leaguecolor)
    table.add_column("Position", style="dim", width=8)
    table.add_column("Team")
    table.add_column("Played", justify="right")
    table.add_column("Won", justify="right")
    table.add_column("Drawn", justify="right")
    table.add_column("Lost", justify="right")
    table.add_column("Points", justify="right", style="bold")
    
    console = Console()
    dicc = {}

    for team in data:
        dicc[data[team]['name']] = data[team]["score"]

    sorteddicc = sorted(dicc, key=dicc.get, reverse=True)
    
    position = 0
    for team in sorteddicc:
        
        #if team is the userteam, make the name bold, else make normal
        position += 1
        if team == userteam:
            table.add_row(str(position), str(data[team]["name"]), str(gameweek), str(data[team]["won"]), str(data[team]["drawn"]), str(data[team]["lost"]), str(data[team]["score"]), style=teamcolor)
        else:    
            table.add_row(str(position), str(data[team]["name"]), str(gameweek), str(data[team]["won"]), str(data[team]["drawn"]), str(data[team]["lost"]), str(data[team]["score"]))
        
    console.print(table)

