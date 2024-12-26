import random
from rich.console import Console
import time
from loading import *

console = Console()

def client_operation(operation, value1, value2,att):
    result = None
    if operation == "add":
        result = value1 + value2

        console.print(f"Client Adding {value2} in {att}: {value1} + {value2} = {result}", style="bold blue")
    elif operation == "subtract":
        result = value1 - value2
        console.print(f"Client Subtracting {value2} in {att} : {value1} - {value2} = {result}", style="bold blue")
    else:
        console.print("Unsupported operation", style="bold red")
    time.sleep(1)
    return result

def generate_random_value():
    return random.randint(1, 100)

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            console.print(f"An error occurred: {str(e)}", style="bold red")
            return None
    return wrapper
