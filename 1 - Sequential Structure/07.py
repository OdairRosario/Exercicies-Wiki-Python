# Make a Program that calculates the area of a square, then show the double of this area to the user

side = float(input("What is the side length in cm?: "))
base = float(input("What is the base length in cm?: "))

area = base * side

print("The area of the square is: ", area, "cm² and the double is:", area * 2,"cm²")
