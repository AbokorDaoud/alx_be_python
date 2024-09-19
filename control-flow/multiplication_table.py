number = int(input('Enter a number to see its multiplication table: '))

for i in range(1, 10+1):  # This will loop through numbers 1 to 10
    product = number * i
    print(f"{number} * {i} = {product}")

    