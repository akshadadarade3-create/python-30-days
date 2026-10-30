"""bank_account.py — deposit(), withdraw() (block overdrafts) and balance()"""
class BankAccount:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self.transactions = []

    def deposit(self, money):
        if money <= 0:
            print("Deposit amount must be positive.")
        else:
            self.amount += money
            self.transactions.append(f"Deposited: {money}")
            print("Deposit successful.")

    def withdraw(self, money):
        if money <= 0:
            print("Withdrawal amount must be positive.")
        elif money > self.amount:
            print("Insufficient balance. Withdrawal blocked.")
        else:
            self.amount -= money
            self.transactions.append(f"Withdrawn: {money}")
            print("Withdrawal successful.")

    def balance(self):
        print("Current balance:", self.amount)

    def show_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)


account1 = BankAccount("Akshada", 1000)
account2 = BankAccount("Sakhi", 3600)

account1.balance()
account1.deposit(500)
account1.balance()
account1.withdraw(300)
account1.balance()
account1.withdraw(2000)
account1.balance()
account1.show_transactions()
