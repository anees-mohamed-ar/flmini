from rich.console import Console
from user_section import UserSection
from admin_section import AdminSection
from encrypt import Encryptor
import os
from time import sleep
from loading import *
from logani import *

console = Console()
encryptor = Encryptor()

class Main:
    def __init__(self):
        self.user_section = UserSection()
        self.admin_section = AdminSection()

    def run(self):
        if not os.path.exists("context.ckks"):
            console.print("Context file not found.", style="bold yellow")
            cla(1,'Creating a new CKKS context')
            CKKS_CONTEXT = encryptor.create_ckks_context()
        else:
            
            CKKS_CONTEXT = encryptor.load_ckks_context()
        while True:
            sleep(1)
            console.print("\nPlease select a role:", style="bold cyan")
            sleep(1)
            console.print("\n[1] User", style="bold green")
            sleep(1)
            console.print("[2] Admin", style="bold green")
            sleep(1)
            console.print("[3] Exit", style="bold red")
            sleep(1)
            choice = input("\nEnter your choice (1/2/3): ")
            print('\n')

            if choice == '1':
                cla(1,'Loading User Interface')
                self.user_section.run()
            elif choice == '2':
                cla(1,'Loading Admin Interface')
                self.admin_section.run()
            elif choice == '3':
                lgn(1,'Exiting.','Exiting..','Exiting...','\nExited')
                sleep(2)
                break
            else:
                sleep(2)
                console.print("Invalid choice. Please try again.", style="bold red")

if __name__ == "__main__":
    main = Main()
    main.run()
