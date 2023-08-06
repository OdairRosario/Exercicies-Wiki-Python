# Make a Program that reads three numbers and shows the largest and smallest one.

num1 = float(input("Value1: "))
num2 = float(input("Value2: "))
num3 = float(input("Value3: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is the largest")
if num1 < num2 and num1 < num3:
    print(f"{num1} is the smallest")

if num2 > num1 and num2 > num3:
    print(f"{num2} is the largest")
if num2 < num1 and num2 < num3:
    print(f"{num2} is the smallest")

if num3 > num1 and num3 > num2:
    print(f"{num3} is the largest")
if num3 < num1 and num3 < num2:
    print(f"{num3} is the smallest")
