# Make a Program that asks for 2 integer numbers and a real number. Calculate and show:
# 1 - the product of the double of the first with half of the second.
# 2 - the sum of the triple of the first with the third.
# 3 - the third raised to the cube.

num1 = int(input("Enter the first number (integer): "))
num2 = int(input("Enter the second number (integer): "))
num3 = float(input("Enter the third number (real): "))

one = (num1*2) + (num2/2)
two = (num1*3) + num3
three = num3**3

print("The product of the double of the first with half of the second: {}".format(one))
print('The sum of the triple of the first with the third: {}'.format(two))
print("The third raised to the cube: {}".format(three))
