# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  # Fahrenheit to Celsius factor
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  # Celsius to Fahrenheit factor

# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main function for user interaction
def main():
    try:
        # Get temperature input
        temperature = float(input("Enter the temperature to convert: "))

        # Get the unit and make sure it's either 'C' or 'F'
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Convert based on the unit
        if unit == "C":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == "F":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            # Raise an error if the unit is invalid
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        # Ensure the error message matches the expected output exactly
        print("Invalid temperature. Please enter a numeric value.")

# Entry point for the script
if __name__ == "__main__":
    main()
