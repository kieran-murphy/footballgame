from rich.console import Console
from rich.table import Table
from rich import inspect

import random
import time
import json

with open('teams.txt') as f:
    data = json.load(f)






def createrichladder(data, leaguecolor, userteam):
    #table.rows = []
    table = Table(show_header=True, header_style=leaguecolor)
    table.add_column("Position", style="dim", width=8)
    table.add_column("Team")
    table.add_column("Points", justify="right")
    console = Console()
    dicc = {}

    for team in data:
        dicc[data[team]['name']] = data[team]["score"]

    sorteddicc = sorted(dicc, key=dicc.get, reverse=True)
    
    position = 0
    for team in sorteddicc:
        
        position += 1
        if team == userteam:
            table.add_row(str(position), str(data[team]["name"]), str(data[team]["score"]), style="wheat1 bold italic")
        else:    
            table.add_row(str(position), str(data[team]["name"]), str(data[team]["score"]))
        
    console.print(table)

#createrichladder(data)


#inspect(Console, methods=True)