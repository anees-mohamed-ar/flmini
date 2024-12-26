import tenseal as ts
import os
from time import sleep
from rich.console import Console
from loading import *
from logani import *

console = Console()

class Encryptor:
    def create_ckks_context(self):
        # Create CKKS context
        CKKS_CONTEXT = ts.context(
            ts.SCHEME_TYPE.CKKS,
            poly_modulus_degree=8192,
            coeff_mod_bit_sizes=[60, 40, 40, 60]
        )
        CKKS_CONTEXT.global_scale = 2 ** 40

        # Generate the keys
        CKKS_CONTEXT.generate_galois_keys()
        CKKS_CONTEXT.generate_relin_keys()

        # Save context with the secret key
        with open("context.ckks", "wb") as f:
            print('\n')
            cla(1,'Writing CKKS Context and Storing Secret Key',message='CKKS Context and Secret Key Created Successfully!!')
            f.write(CKKS_CONTEXT.serialize(save_secret_key=True))

        return CKKS_CONTEXT

    def load_ckks_context(self):
        console.print("[bold cyan]Loading CKKS Context[/bold cyan]" )
        lgn(1,'Loading /','Loading -','Loading |','Load Complete!!')
        print('\n')
        # Load CKKS context with the secret key
        if not os.path.exists("context.ckks"):
            sleep(1)
            raise FileNotFoundError("Context file not found.")

        with open("context.ckks", "rb") as f:
            console.print("[bold cyan]Reading CKKS Context[/bold cyan]")
            lgn(1,'Reading /','Reading -','Reading |','Read Complete!!')
            print('\n')
            CKKS_CONTEXT = ts.context_from(f.read())

        return CKKS_CONTEXT

    def encrypt_data(self, age, income, transactions, context):
        encrypted_age = ts.ckks_vector(context, [age]).serialize()
        encrypted_income = ts.ckks_vector(context, [income]).serialize()
        encrypted_transactions = ts.ckks_vector(context, [transactions]).serialize()
        cla(1,'Encrypting Input Data',message='Input Data Encrypted Successfully')
        return encrypted_age, encrypted_income, encrypted_transactions

    def decrypt_data(self, row, context):
        encrypted_age, encrypted_income, encrypted_transactions = row
        decrypted_age = ts.ckks_vector_from(context, encrypted_age).decrypt()[0]
        decrypted_income = ts.ckks_vector_from(context, encrypted_income).decrypt()[0]
        decrypted_transactions = ts.ckks_vector_from(context, encrypted_transactions).decrypt()[0]
        #cla(1,'Decrypting Data',message='Data Decrypted Successfully')
        return decrypted_age, decrypted_income, decrypted_transactions
