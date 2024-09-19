
positive_integer=int(input('Enter the size of the pattern: '))
current_row = 0  # Start from the first row

while current_row < positive_integer:
    # Nested for loop to print asterisks
    for i in range(positive_integer):
        print("*", end="")
    
    # After printing one row, move to the next line
    print()
    
    # Move to the next row
    current_row += 1
