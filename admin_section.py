from rich.console import Console
from encrypt import Encryptor
from database import db_manager
import time
from loading import *
from logani import *
from time import sleep

console = Console()
encryptor = Encryptor()

a='---------------'
b='***************'
c='xxxxxxxxxxxxxxx'

class AdminSection:
    def authenticate(self):
        attempts = 3
        while attempts > 0:
            password = input("Enter admin password: ")
            if password == "flmini":
                print('\n')
                lgn(1,a,b,c,"Admin Login successful!")
                return True
            else:
                sleep(0.7)
                print('\n')
                console.print(f"Incorrect password. {attempts - 1} attempts remaining.", style="bold red")
                attempts -= 1
                time.sleep(1)
        return False

    def run(self):
        if not self.authenticate():
            sleep(1)
            print('\n')
            console.print("Authentication failed. Exiting Admin Section.", style="bold red")
            return

        CKKS_CONTEXT = encryptor.load_ckks_context()
        db_manager.create_database('encrypted_data.db')  # Ensure database and tables are created
        print('\n')
        console.print("Welcome to the Admin Section!", style="bold cyan")

        while True:
            sleep(1)
            #print('\n')
            console.print("\nChoose an option:", style="bold cyan")
            sleep(0.7)
            console.print("\n[1] View all original data", style="bold green")
            sleep(0.7)
            console.print("[2] View all operated data", style="bold green")
            sleep(0.7)
            console.print("[3] View specific original data by ID", style="bold green")
            sleep(0.7)
            console.print("[4] View specific operated data by ID", style="bold green")
            sleep(0.7)
            console.print("[5] Exit", style="bold red")
            #print('\n')
            sleep(0.7)
            choice = input("\nEnter your choice (1/2/3/4/5): ")

            if choice == '1':
                data = db_manager.fetch_all_data('encrypted_data.db', 'original_data')
                decrypted_data = [(row[0], row[1], *encryptor.decrypt_data(row[2:], CKKS_CONTEXT)) for row in data]
                print('\n')
                cla(1,'Decrypting data for Table',message='Decrypted Table Ready to Print!')
                sleep(1)
                db_manager.print_data_table(decrypted_data, "Original Data")
            elif choice == '2':
                data = db_manager.fetch_all_data('encrypted_data.db', 'operated_data')
                decrypted_data = [(row[0], row[1], *encryptor.decrypt_data(row[2:], CKKS_CONTEXT)) for row in data]
                print('\n')
                cla(1,'Decrypting data for Table',message='Decrypted Table Ready to Print!')
                sleep(1)
                db_manager.print_data_table(decrypted_data, "Operated Data")
            elif choice == '3':
                data_id = input("Enter data ID: ")
                sleep(0.5)
                row = db_manager.fetch_data_by_id('encrypted_data.db', 'original_data', data_id)
                if row:
                    print('\n')
                    lgn(1,'Decrypting data for Table /','Decrypting data for Table -','Decrypting data for Table |','Done!!')
                    decrypted_row = (row[0], row[1], *encryptor.decrypt_data(row[2:], CKKS_CONTEXT))
                    sleep(0.5)
                    db_manager.print_data_table([decrypted_row], "Original Data")
                else:
                    print('\n')
                    sleep(1)
                    console.print("Data ID not found.", style="bold red")
                    sleep(0.5)
            elif choice == '4':
                print('\n')
                data_id = input("Enter data ID: ")
                row = db_manager.fetch_data_by_id('encrypted_data.db', 'operated_data', data_id)
                if row:
                    lgn(1,'Decrypting data for Table /','Decrypting data for Table -','Decrypting data for Table |','Done!!')
                    decrypted_row = (row[0], row[1], *encryptor.decrypt_data(row[2:], CKKS_CONTEXT))
                    db_manager.print_data_table([decrypted_row], "Operated Data")
                else:
                    sleep(1)
                    console.print("Data ID not found.", style="bold red")
                    sleep(0.5)
            elif choice == '5':
                lgn(1,'Exiting.','Exiting..','Exiting...','Exited Admin Section')
                #console.print("Exiting Admin Section.", style="bold yellow")
                break
            else:
                sleep(0.7)
                console.print("Invalid choice. Please try again.", style="bold red")
                sleep(0.7)
