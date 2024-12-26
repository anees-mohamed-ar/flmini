from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
import time

console = Console()

def cla(duration,content,message='Done!'):
    with Progress(
        SpinnerColumn(),
        "[progress.description]{task.description}",
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f} %"),
        transient=True
    ) as progress:
        task = progress.add_task(f"[bold cyan]{content}...", total=100)
        lizer=int(100/duration)
        for _ in range(duration * lizer ):
            progress.update(task, advance=1)
            time.sleep(0.1)
        progress.update(task, completed=100)
        console.print(f"[bold green]  {message}", style="bold green")

# Example usage

