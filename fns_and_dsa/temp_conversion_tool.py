# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Factor for Fahrenheit to Celsius conversion
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Factor for Celsius to Fahrenheit conversion
CELSIUS_OFFSET = 32  # The offset used for conversion between Celsius and Fahrenheit

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - CELSIUS_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + CELSIUS_OFFSET
    return fahrenheit

# Main function to handle user interaction
def main():
    try:
        # Get user input for the temperature
        temperature = float(input("Enter the temperature to convert: "))
        
        # Get the temperature unit (Celsius or Fahrenheit)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'F':
            # Convert Fahrenheit to Celsius
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")
        elif unit == 'C':
            # Convert Celsius to Fahrenheit
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")
        else:
            # If the user enters an invalid unit
            print("Invalid input. Please specify 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        # Handle invalid input for temperature
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
