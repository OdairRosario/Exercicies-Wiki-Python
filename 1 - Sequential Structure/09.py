# Make a Program that asks for the temperature in Fahrenheit degrees, transform and show the temperature in Celsius degrees. C = 5 * ((F-32) / 9).

tempF = int(input("Temperature in Fahrenheit degrees: "))

tempC = 5 * ((tempF-32) / 9)

print("{0} degrees Fahrenheit in Celsius degrees: {1}".format(tempF, tempC))
