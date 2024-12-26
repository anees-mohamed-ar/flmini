from rich.console import Console
from rich.spinner import Spinner
import time

console = Console()

def lgn(duration,one,two,three,message):
    with console.status("[bold cyan]Logging in...") as status:
        for _ in range(duration * 5):
            time.sleep(0.2)
            status.update(f"[bold blue]{one}")
            time.sleep(0.2)
            status.update(f"[bold magenta]{two}")
            time.sleep(0.2)
            status.update(f"[bold green]{three}")
    
    console.print(f"[bold green]{message}", style="bold green")

# Example usage
#   # Adjust the duration as needed
