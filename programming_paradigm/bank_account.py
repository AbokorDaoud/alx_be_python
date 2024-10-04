class BankAccount:
    def __init__(self, balance_file="balance.txt"):
        self.balance_file = balance_file
        self.balance = self.load_balance()

    def load_balance(self):
        """Load the balance from a file, or return 0 if the file doesn't exist."""
        try:
            with open(self.balance_file, "r") as file:
                return float(file.read())
        except FileNotFoundError:
            return 0.0

    def save_balance(self):
        """Save the current balance to a file."""
        with open(self.balance_file, "w") as file:
            file.write(str(self.balance))

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            self.save_balance()
            return f"Deposited: ${amount:.2f}"

    def withdraw(self, amount):
        """Withdraw money from the account if sufficient balance is available."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.save_balance()
            return f"Withdrew: ${amount:.2f}"
        else:
            return "Insufficient funds"

    def display_balance(self):
        """Display the current balance."""
        return f"Current Balance: ${self.balance:.2f}"
