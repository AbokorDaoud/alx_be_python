# Step 1: Prompt for User Input
num1 = float(input("Enter the first number: "))  # Convert input to float for calculations
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Step 2: Perform the Calculation Using Match Case
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:  # Check for division by zero
            result = num1 / num2
        else:
            result = "Cannot divide by zero."

# Step 3: Output the Result
if isinstance(result, str):  # If the result is a string (error message)
    print(result)
else:
    print(f"The result is : {result}.")
