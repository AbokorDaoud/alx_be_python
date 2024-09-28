def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Start with an empty list
    while True:
        display_menu()  # Show menu options
        try:
            choice = int(input("Enter your choice: "))  # Get user input as a number

            if choice == 1:  # Add item
                item = input("Enter the item name: ")  # Ask for the item to add
                shopping_list.append(item)  # Add the item to the list
                print(f"{item} has been added to your shopping list.")

            elif choice == 2:  # Remove item
                item = input("Enter the item name to remove: ")  # Ask for the item to remove
                if item in shopping_list:  # Check if the item is in the list
                    shopping_list.remove(item)  # Remove the item
                    print(f"{item} has been removed from your shopping list.")
                else:
                    print(f"{item} not found in the shopping list.")  # If the item doesn't exist

            elif choice == 3:  # View list
                if not shopping_list:  # Check if the list is empty
                    print("Your shopping list is empty.")
                else:
                    print("Your shopping list:")
                    for item in shopping_list:  # Loop through the list and print each item
                        print(f"- {item}")

            elif choice == 4:  # Exit
                print("Goodbye!")
                break  # Exit the loop, ending the program

            else:
                print("Invalid choice. Please try again.")
        
        except ValueError:
            print("Please enter a valid number.")  # Handle non-integer inputs

if __name__ == "__main__":
    main()
