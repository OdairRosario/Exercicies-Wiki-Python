# Make a Program that asks for the temperature in Celsius degrees, transform and show in Fahrenheit degrees.

tempC = float(input("Temperature in Celsius: "))

tempF = tempC * (9/5) + 32
print(f"{tempC} degrees Celsius in Fahrenheit: {tempF}")
