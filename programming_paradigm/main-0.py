import sys
from bank_account import BankAccount

# Initialize the BankAccount with balance persistence
account = BankAccount()

if __name__ == "__main__":
    # Check if there is any command-line argument
    if len(sys.argv) == 2:
        action = sys.argv[1]
        
        # Check if the action is 'deposit' or 'withdraw' with an amount
        if "deposit" in action:
            try:
                amount = float(action.split(":")[1])
                print(account.deposit(amount))
            except ValueError:
                print("Invalid amount. Please enter a valid number for deposit.")
        
        elif "withdraw" in action:
            try:
                amount = float(action.split(":")[1])
                print(account.withdraw(amount))
            except ValueError:
                print("Invalid amount. Please enter a valid number for withdrawal.")
        
        # Check if the action is 'display'
        elif action == "display":
            print(account.display_balance())
        else:
            print("Invalid command. Use 'deposit:<amount>', 'withdraw:<amount>', or 'display'.")
    else:
        print("Usage: python main-0.py [action:amount] or display")
