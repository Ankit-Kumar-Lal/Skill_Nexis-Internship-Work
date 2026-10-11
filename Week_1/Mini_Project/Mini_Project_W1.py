# Simple ATM Simulator

balance = 1000
pin = 1234

def check_balance():
    print("Current balance:", balance)

def deposit():
    global balance
    amount = float(input("Enter deposit amount: "))
    if amount > 0:
        balance = balance + amount
        print("Amount deposited successfully!")
    else:
        print("Invalid amount")

def withdraw():
    global balance
    amount = float(input("Enter withdrawal amount: "))
    if amount > 0 and amount <= balance:
        balance = balance - amount
        print("Please collect your cash")
    else:
        print("Insufficient balance or invalid amount")

user_pin = int(input("Enter your PIN: "))

if user_pin == pin:
    print("Login successful!")

    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice")
else:
    print("Incorrect PIN")
