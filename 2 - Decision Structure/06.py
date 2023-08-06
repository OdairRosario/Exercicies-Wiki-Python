# Make a Program that reads three numbers and shows the largest one.

num1 = float(input("Value 1: "))
num2 = float(input("Value 2: "))
num3 = float(input("Value 3: "))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} is the largest")
    else:
        print(f"{num3} is the largest")
elif num2 > num1:
    if num2 > num3:
        print(f"{num2} is the largest")
    else:
        print(f"{num3} is the largest")
