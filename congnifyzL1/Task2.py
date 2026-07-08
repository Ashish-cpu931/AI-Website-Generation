# Temperature Conversion

temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()

if unit == "C":
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature}°C = {fahrenheit:.2f}°F")

elif unit == "F":
    celsius = (temperature - 32) * 5/9
    print(f"{temperature}°F = {celsius:.2f}°C")

else:
    print("Invalid unit! Please enter 'C' for Celsius or 'F' for Fahrenheit.")