# Make a Program that reads three numbers and shows them in descending order.

num1 = float(input("Value1: "))
num2 = float(input("Value2: "))
num3 = float(input("Value3: "))

if num1 > num2 and num1 > num3:
    print(num1)
    if num2 > num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
if num2 > num1 and num2 > num3:
    print(num2)
    if num1 > num3:
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
if num3 > num1 and num3 > num2:
    print(num3)
    if num1 > num2:
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)
