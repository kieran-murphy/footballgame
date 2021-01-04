from rich.console import Console
from rich.table import Table
import random
import time
import json

with open('teams.txt') as f:
    data = json.load(f)

console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Position", style="dim", width=12)
table.add_column("Team")
table.add_column("Points", justify="right")

def createrichladder(data):

    dicc = {}

    for team in data:
        dicc[data[team]['name']] = data[team]["score"]

    sorteddicc = sorted(dicc, key=dicc.get, reverse=True)
    
    position = 0
    for team in sorteddicc:
        
        position += 1
        table.add_row(str(position), str(data[team]["name"]), str(data[team]["score"]))
        
    console.print(table)
createrichladder(data)

