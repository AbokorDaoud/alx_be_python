from datetime import datetime, timedelta  # Import datetime and timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date and time
    print(f"Current date and time: {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        # Ask the user for the number of days to add to the current date
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()  # Get the current date and time
        future_date = current_date + timedelta(days=days_to_add)  # Add days to the current date
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")  # Display the future date in YYYY-MM-DD format
    except ValueError:
        # Handle the case when the input is not a valid integer
        print("Invalid input. Please enter a valid number of days.")

# Main function to call the above two functions
def main():
    display_current_datetime()  # Call the function to display current date and time
    calculate_future_date()  # Call the function to calculate and display future date

# Entry point of the script
if __name__ == "__main__":
    main()
