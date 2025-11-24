FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def  convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


temperature = input('Enter the temperature to convert: ')

if type(temperature) == float | int :
    print('Invalid temperature. Please enter a numeric value.')
else:
    factor = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').strip().upper()

    # Perform conversion based on unit
    if factor == 'F':
        converted_temp = convert_to_celsius(float(temperature))
        print(f"{temperature}°F is equal to {converted_temp:.2f}°C")
    elif factor == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")