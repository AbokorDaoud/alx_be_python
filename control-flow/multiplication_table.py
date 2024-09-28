# Ask the user to input a number
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to iterate through numbers 1 to 10
for i in range(1, 11):
    # Print the multiplication table in the exact required format
    print(f"{number} * {i} = {number * i}")


    