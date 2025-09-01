class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(amount, "deposited.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(amount, "withdrawn.")
        else:
            print("Not enough balance!")

    def check_balance(self):
        print("Current balance:", self.balance)
name = input("Enter your name: ")
start_balance = int(input("Enter starting balance: "))
account = BankAccount(name, start_balance)
while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        amount = int(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == "2":
        amount = int(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == "3":
        account.check_balance()
    elif choice == "4":
        print("Thank you for using the bank system!")
        break
    else:
        print("Invalid choice, try again.")
