def miles_to_kilometers(miles):
    return miles * 1.60934

# Example usage:
miles = float(input("Enter distance in miles: "))
kilometers = miles_to_kilometers(miles)
print(f"{miles} miles is equal to {kilometers} kilometers")


def kilometers_to_miles(kilometers):
    return kilometers / 1.60934

# Example usage:
kilometers = float(input("Enter distance in kilometers: "))
miles = kilometers_to_miles(kilometers)
print(f"{kilometers} kilometers is equal to {miles} miles")


def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Example usage:
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Example usage:
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F is equal to {celsius}°C")

