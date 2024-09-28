# Function to display the menu
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Main function to manage the shopping list
def main():
    shopping_list = []  # Initialize an empty shopping list
    
    while True:
        display_menu()  # Show the menu options
        choice = input("Enter your choice: ")  # Get the user's choice
        
        if choice == '1':  # Add an item to the list
            item = input("Enter the item name: ")
            shopping_list.append(item)  # Add the item to the shopping list
        
        elif choice == '2':  # Remove an item from the list
            item = input("Enter the item name to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)  # Remove the item if it exists
            else:
                print("Item not found in the shopping list.")
        
        elif choice == '3':  # View the current shopping list
            if not shopping_list:  # Check if the list is empty
                print("Your shopping list is empty.")
            else:
                print("Your shopping list:")
                for item in shopping_list:
                    print(f"- {item}")
        
        elif choice == '4':  # Exit the program
            print("Goodbye!")
            break  # Exit the loop
        
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

# Run the main function
if __name__ == "__main__":
    main()
