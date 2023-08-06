# Given a person's height as input data, construct an algorithm that calculates their ideal weight, using the following formula: (72.7*height) - 58

height = int(input("Enter your height in cm: "))
height = height / 100

idealWeight = (72.7*height) - 58

print("Your ideal weight is:", idealWeight)
