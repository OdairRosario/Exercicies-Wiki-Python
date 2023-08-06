# Make a Program that asks for the radius of a circle, calculate and show its area.

radius = float(input("What is the radius of the circle in cm? :"))
pi = 3.14

radius_squared = radius * radius

area = pi * radius_squared

print("The area of the circle is:", area," m²")
