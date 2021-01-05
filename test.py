from rich import print
from rich.table import Table

grid = Table.grid(expand=True)
grid.add_column()
grid.add_column(justify="left")
grid.add_row("Raising shields", "[bold magenta]COMPLETED [green]:heavy_check_mark:")
grid.add_row("Raising shields", "[bold magenta]COMPLETED [green]:heavy_check_mark:")
grid.add_row("Raising shields", "[bold magenta]COMPLETED [green]:heavy_check_mark:")
grid.add_row("Raising shields", "[bold magenta]COMPLETED [green]:heavy_check_mark:")
grid.add_row("Raising shields", "[bold magenta]COMPLETED [green]:heavy_check_mark:")

print(grid)