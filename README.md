# Federated Learning with CKKS Encryption

## Description

This project aims to enhance privacy in a federated learning system using the CKKS encryption scheme. The system allows users to input data, which is then encrypted and processed. Admins can view both the original and operated encrypted data.

## Requirements

- Python 3.8 or higher

### Install necessary packages:

```bash
pip install -r requirements.txt
```

## Files

- **main.py**: Manages the overall flow, allowing users to switch between User and Admin sections.
- **encrypt.py**: Handles encryption and decryption using the TenSEAL library.
- **database.py**: Manages database operations, including creating the database, inserting data, and fetching data.
- **utils.py**: Provides utility functions for client operations and exception handling.
- **user_section.py**: Manages the User section, including data input, client operations, and storing data.
- **admin_section.py**: Manages the Admin section, including authentication, viewing data, and decrypting data.
- **rich_print.py**: Enhances terminal output using the rich library.

## Instructions

### Run `main.py`:

```bash
python main.py
```

### Choose a role:

- [1] User
- [2] Admin
- [3] Exit

#### User Role:

- [1] Input data to test
- [2] Exit to role menu

Input name, age, income, and transactions.

Choose to automate client operations or enter manual values.

The data inputted will be distributed to clients for operation.

Encrypted data is stored in the original_data table.

Operated encrypted data is stored in the operated_data table.

#### Admin Role:

Authenticate using the admin password (flmini).

View original and operated data.

View specific data by ID.

## Examples

Running the program:

```bash
python main.py
```

## Notes

Ensure the `context.ckks` file is present, or it will be created.

The admin password is **flmini**.

