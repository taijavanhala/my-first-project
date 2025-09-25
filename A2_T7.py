print("Program starting.")

fahrenheit = float(input("Insert fahrenheits: "))
celsius = (fahrenheit - 32) / 1.8
celsius = round(celsius, 1)

print(f"{fahrenheit:.1f}°F is {celsius:.1f}°C")

print("Program ending.")
