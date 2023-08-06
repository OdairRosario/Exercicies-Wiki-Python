# Make a Program that asks for two numbers and prints the largest one.

num1 = float(input("Enter a value: "))
num2 = float(input("Enter a value: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")
