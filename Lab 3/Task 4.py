# Global dictionary to store user credentials
users_db = {}

def register_user():
    """
    Register a new user by adding username and password to users_db dictionary.
    
    Returns:
        bool: True if registration successful, False otherwise
    """
    print("\n=== USER REGISTRATION ===")
    
    # Get username
    username = input("Enter username: ").strip()
    
    # Check if username already exists
    if username in users_db:
        print("Error: Username already exists!")
        return False
    
    # Validate username
    if len(username) < 3:
        print("Error: Username must be at least 3 characters long!")
        return False
    
    # Get password
    password = input("Enter password: ").strip()
    
    # Validate password
    if len(password) < 6:
        print("Error: Password must be at least 6 characters long!")
        return False
    
    # Confirm password
    confirm_password = input("Confirm password: ").strip()
    
    if password != confirm_password:
        print("Error: Passwords do not match!")
        return False
    
    # Store user credentials
    users_db[username] = password
    print(f"Success: User '{username}' registered successfully!")
    return True


def login_user():
    """
    Authenticate a user by checking username and password against users_db dictionary.
    
    Returns:
        bool: True if login successful, False otherwise
    """
    print("\n=== USER LOGIN ===")
    
    # Get username
    username = input("Enter username: ").strip()
    
    # Check if username exists
    if username not in users_db:
        print("Error: Username not found!")
        return False
    
    # Get password
    password = input("Enter password: ").strip()
    
    # Check if password matches
    if users_db[username] == password:
        print(f"Success: Welcome back, {username}!")
        return True
    else:
        print("Error: Incorrect password!")
        return False


def display_users():
    """
    Display all registered users (for demonstration purposes).
    """
    print("\n=== REGISTERED USERS ===")
    if not users_db:
        print("No users registered yet.")
    else:
        for username in users_db.keys():
            print(f"Username: {username}")
    print("=" * 25)


def main():
    """
    Main function to demonstrate user registration and login system.
    """
    print("User Authentication System")
    print("=" * 30)
    
    while True:
        print("\nChoose an option:")
        print("1. Register new user")
        print("2. Login user")
        print("3. Display all users")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            display_users()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-4.")


def demo_registration_and_login():
    """
    Demonstrate the registration and login functions with example users.
    """
    print("Demo: Registration and Login System")
    print("=" * 40)
    
    # Demo registration
    print("\n--- Demo Registration ---")
    
    # Simulate user registration
    test_users = [
        ("john_doe", "password123"),
        ("jane_smith", "secure456"),
        ("admin", "admin123")
    ]
    
    for username, password in test_users:
        if username not in users_db:
            users_db[username] = password
            print(f"Registered: {username}")
    
    # Demo login
    print("\n--- Demo Login ---")
    
    # Test successful login
    test_username = "john_doe"
    test_password = "password123"
    
    if test_username in users_db and users_db[test_username] == test_password:
        print(f"Login successful for: {test_username}")
    else:
        print(f"Login failed for: {test_username}")
    
    # Test failed login
    wrong_password = "wrongpass"
    if test_username in users_db and users_db[test_username] == wrong_password:
        print(f"Login successful for: {test_username}")
    else:
        print(f"Login failed for: {test_username} (wrong password)")


if __name__ == "__main__":
    # Run demo first
    demo_registration_and_login()
    
    # Then run interactive system
    print("\n" + "=" * 50)
    main()
