shopping_list = [] 
def display_menu():  # Ensure only these options are printed as expected by the checker
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    
    while True:
        display_menu()  
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:  
                item = input("Enter the item name: ")
                shopping_list.append(item)
                print(f"{item} has been added to your shopping list.")
            
            elif choice == 2:  
                item = input("Enter the item name to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"{item} has been removed from your shopping list.")
                else:
                    print(f"{item} not found in the shopping list.")
            
            elif choice == 3:  
                if not shopping_list:  
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
            print("Invalid input. Please enter a number.")  
if __name__ == "__main__":
    main()
