import hashlib

# Dictionary to store user credentials
users = {}

def register():
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Please choose a different one.")
        return
    password = input("Enter a password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[username] = hashed_password
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in users and users[username] == hashed_password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

def secured_page():
    print("Welcome to the secured page!")

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            if login():
                secured_page()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
