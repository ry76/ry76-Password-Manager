from cryptography.fernet import Fernet
import json
import os

# Function to generate key for encryption
def generate_key():
    return Fernet.generate_key()

# Function to save key to a file (used later to decrypt)
def save_key(key):
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Function to load previously generated key
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt password
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Function to decrypt password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Function to add password 
def add_password(service, password, key):
    encrypted_password = encrypt_password(password, key)
    # Save the encrypted password in dictionary
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            data = json.load(file)
    else:
        data = {}

    data[service] = encrypted_password.decode()

    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)

# Function to get password 
def get_password(service, key):
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)

        encrypted_password = data.get(service)
        if encrypted_password:
            encrypted_password = encrypted_password.encode()
            return decrypt_password(encrypted_password, key)
        else:
            print("Service not found.")
    except FileNotFoundError:
        print("No passwords stored yet.")
    return None

# Main function to run the password manager
def run_password_manager():
    if not os.path.exists("secret.key"):
        key = generate_key()
        save_key(key)
    else:
        key = load_key()

    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            service = input("Enter service name: ")
            password = input("Enter password: ")
            add_password(service, password, key)
            print(f"Password for {service} has been added securely.")

        elif choice == "2":
            service = input("Enter service name to retrieve password: ")
            password = get_password(service, key)
            if password:
                print(f"Password for {service}: {password}")

        elif choice == "3":
            print("Exiting password manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_password_manager()

