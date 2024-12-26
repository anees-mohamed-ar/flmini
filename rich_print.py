from rich.console import Console
from rich.table import Table
import time

console = Console()

def print_table(data, title):
    table = Table(title=title)
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Name", style="magenta")
    table.add_column("Age", style="green")
    table.add_column("Income", style="green")
    table.add_column("Transactions", style="green")

    for row in data:
        table.add_row(str(row[0]), row[1], str(row[2]), str(row[3]), str(row[4]))

    console.print(table)
    time.sleep(1)

def print_message(message, style="bold green"):
    console.print(message, style=style)
    time.sleep(1)
