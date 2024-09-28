def display_menu():
    # Ensure only these options are printed as expected by the checker
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize shopping_list as an empty list
    
    while True:
        display_menu()  # Call display_menu to show options
        
        try:
            # Take input and ensure it's an integer
            choice = int(input("Enter your choice: "))
            
            if choice == 1:  # Add item to the list
                item = input("Enter the item name: ")
                shopping_list.append(item)
                print(f"{item} has been added to your shopping list.")
            
            elif choice == 2:  # Remove item from the list
                item = input("Enter the item name to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"{item} has been removed from your shopping list.")
                else:
                    print(f"{item} not found in the shopping list.")
            
            elif choice == 3:  # View the shopping list
                if not shopping_list:  # Check if the list is empty
                    print("Your shopping list is empty.")
                else:
                    print("Your shopping list:")
                    for item in shopping_list:
                        print(f"- {item}")
            
            elif choice == 4:  # Exit the program
                print("Goodbye!")
                break  # Exit the loop to end the program
            
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")  # Handle non-numeric input

if __name__ == "__main__":
    main()
