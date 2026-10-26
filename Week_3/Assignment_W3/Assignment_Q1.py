# Bank Account Class

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print(f"Rs. {amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Rs. {amount:.2f} withdrawn successfully.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: Rs. {self.balance:.2f}")


# Main program
account = BankAccount("Ankit", 5000)

account.display_balance()
account.deposit(2000)
account.withdraw(1500)
account.display_balance()
