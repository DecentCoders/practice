class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Private attribute (encapsulation)

    # Deposit money (validate positive amount)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Error: Deposit amount must be positive!")

    # Withdraw money (validate sufficient balance)
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Error: Invalid withdrawal amount (insufficient balance or negative)!")

    # Getter method to access private balance (controlled access)
    def get_balance(self):
        return self.__balance

# Test
account = BankAccount(100)
account.deposit(50)  # Balance: 150
account.withdraw(75) # Balance: 75
account.withdraw(100) # Error (insufficient balance)
print(f"Final Balance: ${account.get_balance()}")  # 75
# print(account.__balance) → Error (private attribute cannot be accessed directly)