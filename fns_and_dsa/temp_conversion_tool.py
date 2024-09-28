# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  # Fahrenheit to Celsius conversion factor
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  # Celsius to Fahrenheit conversion factor

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main function to interact with the user
def main():
    try:
        # Get the temperature from the user
        temperature = float(input("Enter the temperature to convert: "))

        # Ask whether the input is Celsius or Fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform conversion based on the user's input
        if unit == "C":
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == "F":
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            # If the unit is not 'C' or 'F', raise a ValueError
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError as e:
        # Handle invalid temperature input or invalid unit input
        print(f"Invalid input: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
