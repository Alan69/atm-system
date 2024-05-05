import datetime

class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def display_balance(self):
        print(f"Account Balance: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.add_transaction("Deposit", amount)
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.add_transaction("Withdrawal", amount)
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient funds.")

    def transfer(self, destination_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            destination_account.balance += amount
            self.add_transaction("Transfer to " + destination_account.account_number, amount)
            destination_account.add_transaction("Transfer from " + self.account_number, amount)
            print(f"${amount} transferred successfully.")
        else:
            print("Insufficient funds.")

    def change_pin(self, new_pin):
        self.pin = new_pin
        print("PIN changed successfully.")

    def add_transaction(self, transaction_type, amount):
        timestamp = datetime.datetime.now()
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "timestamp": timestamp
        }
        self.transaction_history.append(transaction)

    def display_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(f"{transaction['timestamp']}: {transaction['type']} ${transaction['amount']}")


class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, pin, initial_balance=0):
        if account_number not in self.accounts:
            account = Account(account_number, pin, initial_balance)
            self.accounts[account_number] = account
            print("Account created successfully.")
        else:
            print("Account number already exists.")

    def authenticate(self, account_number, pin):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            if account.pin == pin:
                return account
        return None

    def display_menu(self):
        print("1. Display Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer Funds")
        print("5. Change PIN")
        print("6. Transaction History")
        print("7. Exit")

    def run(self):
        while True:
            print("\nWelcome to the ATM")
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")

            account = self.authenticate(account_number, pin)
            if account:
                print("Login successful.")
                while True:
                    self.display_menu()
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        account.display_balance()
                    elif choice == "2":
                        amount = float(input("Enter deposit amount: $"))
                        account.deposit(amount)
                    elif choice == "3":
                        amount = float(input("Enter withdrawal amount: $"))
                        account.withdraw(amount)
                    elif choice == "4":
                        destination_account_number = input("Enter destination account number: ")
                        destination_account = self.accounts.get(destination_account_number)
                        if destination_account:
                            amount = float(input("Enter transfer amount: $"))
                            account.transfer(destination_account, amount)
                        else:
                            print("Destination account not found.")
                    elif choice == "5":
                        new_pin = input("Enter new PIN: ")
                        account.change_pin(new_pin)
                    elif choice == "6":
                        account.display_transaction_history()
                    elif choice == "7":
                        print("Thank you for using the ATM. Goodbye!")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid account number or PIN. Please try again.")


if __name__ == "__main__":
    atm = ATM()
    atm.create_account("123456", "1234", 1000)
    atm.create_account("789012", "5678", 500)
    atm.run()
