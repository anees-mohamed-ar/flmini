from rich.console import Console
from encrypt import Encryptor
from database import db_manager
from utils import generate_random_value, handle_exceptions
import tenseal as ts
import time
from loading import *
from time import sleep

console = Console()
encryptor = Encryptor()

class UserSection:
    @handle_exceptions
    def run(self):
        while True:
            console.print("\nWelcome to the User Section!", style="bold cyan")
            sleep(0.7)
            console.print('\n[bold yellow]Menu : ')
            sleep(0.7)
            console.print('\n[bold cyan]1.Input Data To Test : ')
            sleep(0.7)
            console.print('[bold red]2.Back to Role Menu : ')
            sleep(0.7)
            i=input('Enter Your Choice (1/2): ')
            sleep(1)
            if i=='1':
                CKKS_CONTEXT = encryptor.load_ckks_context()
                db_manager.create_database('encrypted_data.db')  # Ensure database and tables are created
                sleep(0.5)
                console.print("Enter Raw Data to [bold red]Distribute to Client![/bold red]\n", style="bold cyan")
                sleep(1.5)
                name = input("Enter your name: ")
                age = int(input("Enter your age: "))
                income = int(input("Enter your income: "))
                transactions = int(input("Enter your transactions: "))

                # Encrypt data right after user input
                encrypted_age = ts.ckks_vector(CKKS_CONTEXT, [age])
                encrypted_income = ts.ckks_vector(CKKS_CONTEXT, [income])
                encrypted_transactions = ts.ckks_vector(CKKS_CONTEXT, [transactions])
                cla(1,'Encrypting Input Data',message='Input Data Encrypted')
                # Store original encrypted data
                encrypted_original_data = (
                    encrypted_age.serialize(),
                    encrypted_income.serialize(),
                    encrypted_transactions.serialize()
                )

                db_manager.insert_data('encrypted_data.db', 'original_data', name, encrypted_original_data)
                
                console.print("Choose client operation mode:", style="bold cyan")
                sleep(0.5)
                console.print("[1] Automate client operation", style="bold green")
                sleep(0.5)
                console.print("[2] Enter manual values for client operation", style="bold green")
                sleep(0.5)
                operation_choice = input("Enter your choice (1/2): ")

                if operation_choice == '1':
                    value = generate_random_value()
                    sleep(1)
                    console.print(f"Adding {value} to age", style="bold blue")
                    encrypted_age += value
                    
                    value = generate_random_value()
                    sleep(1)
                    console.print(f"Subtracting {value} from income", style="bold blue")
                    encrypted_income -= value
                    
                    value = generate_random_value()
                    sleep(1)
                    console.print(f"Adding {value} to transactions", style="bold blue")
                    encrypted_transactions += value

                elif operation_choice == '2':
                    console.print("Manual client operation mode:", style="bold cyan")
                    value1 = int(input("Enter value for age operation: "))
                    sleep(0.5)
                    console.print(f"Adding {value1} to age", style="bold blue")
                    encrypted_age += value1
                    
                    value2 = int(input("Enter value for income operation: "))
                    sleep(0.5)
                    console.print(f"Subtracting {value2} from income", style="bold blue")
                    encrypted_income -= value2
                    
                    value3 = int(input("Enter value for transactions operation: "))
                    sleep(0.5)
                    console.print(f"Adding {value3} to transactions", style="bold blue")
                    encrypted_transactions += value3
                else:
                    sleep(0.5)
                    console.print("Invalid choice. Proceeding without client operation.", style="bold red")

                # Serialize operated encrypted data for storage
                encrypted_operated_data = (
                    encrypted_age.serialize(),
                    encrypted_income.serialize(),
                    encrypted_transactions.serialize()
                )

                db_manager.insert_data('encrypted_data.db', 'operated_data', name, encrypted_operated_data)
                sleep(1)
                console.print("\nOperated data encrypted and stored successfully.", style="bold green")
                time.sleep(1)

            elif i=='2':
                break

            else:
                sleep(1)
                console.print("\nInvalid choice. Please try again.", style="bold red")
                sleep(1)
