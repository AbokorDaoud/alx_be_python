def display_menu():
    # Ensure your function definition is exactly as follows
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    # Ensure the list is initialized as an empty array
    shopping_list = []  
    
    while True:
        # Call display_menu before asking for input
        display_menu()
        
        try:
            # Ensure input is being taken as a number
            choice = int(input("Enter your choice: "))
            
            if choice == 1:  # Add item
                item = input("Enter the item name: ")
                shopping_list.append(item)
                print(f"{item} has been added to your shopping list.")

            elif choice == 2:  # Remove item
                item = input("Enter the item name to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"{item} has been removed from your shopping list.")
                else:
                    print(f"{item} not found in the shopping list.")

            elif choice == 3:  # View list
                if not shopping_list:
                    print("Your shopping list is empty.")
                else:
                    print("Your shopping list:")
                    for item in shopping_list:
                        print(f"- {item}")

            elif choice == 4:  # Exit
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            # Handle non-numeric input
            print("Please enter a valid number.")
            
if __name__ == "__main__":
    main()
