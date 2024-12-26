import sqlite3
from rich.console import Console
from rich.table import Table
import time
from time import sleep
from loading import *
from logani import *

console = Console()

class DatabaseManager:
    def create_database(self, db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS original_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            encrypted_age BLOB,
            encrypted_income BLOB,
            encrypted_transactions BLOB
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS operated_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            encrypted_age BLOB,
            encrypted_income BLOB,
            encrypted_transactions BLOB
        )
        ''')
        conn.commit()
        conn.close()

    def insert_data(self, db_path, table, name, encrypted_data):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(f'''
        INSERT INTO {table} (name, encrypted_age, encrypted_income, encrypted_transactions)
        VALUES (?, ?, ?, ?)
        ''', (name, *encrypted_data))
        conn.commit()
        sleep(0.7)
        lgn(1,'Inserting Encrypted Data to Database /','Inserting Encrypted Data to Database -','Inserting Encrypted Data to Database |','Data Inserted to Database Successfuly')
        conn.close()
        sleep(0.5)

    def fetch_all_data(self, db_path, table):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {table}')
        rows = cursor.fetchall()
        cla(1,f'Fetching {table} From Database({db_path})',message='Fetch Complete!!')
        conn.close()
        return rows

    def fetch_data_by_id(self, db_path, table, data_id):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {table} WHERE id = ?', (data_id,))
        row = cursor.fetchone()
        lgn(1,'Searching For ID /','Searching For ID -','Searching For ID |','Search Complete')
        conn.close()
        return row

    def print_data_table(self, data, title):
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
        x=input('Press enter')

db_manager = DatabaseManager()
