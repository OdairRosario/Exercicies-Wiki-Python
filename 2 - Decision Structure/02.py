# Make a Program that asks for a value and shows on the screen whether the value is positive or negative.

num1 = float(input("Enter a value: "))

if num1 < 0:
    print(f"{num1} is negative")
elif num1 == 0:
    print("0 (zero) is neutral/null")
else:
    print(f"{num1} is positive")
