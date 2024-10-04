class BankAccount:
    def __init__(self, balance_file="balance.txt"):
        self.balance_file = balance_file
        self.balance = self.load_balance()

    def load_balance(self):
        try:
            with open(self.balance_file, "r") as file:
                return float(file.read())
        except FileNotFoundError:
            return 0.0

    def save_balance(self):
        with open(self.balance_file, "w") as file:
            file.write(str(self.balance))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.save_balance()
            # Formatting to two decimal places and exact wording
            return f"Deposited: ${amount:.2f}"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.save_balance()
            # Formatting to two decimal places and exact wording
            return f"Withdrew: ${amount:.2f}"
        else:
            return "Insufficient funds"

    def display_balance(self):
        # Formatting the balance to two decimal places and exact wording
        return f"Current Balance: ${self.balance:.2f}"
