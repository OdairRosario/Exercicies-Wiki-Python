# Create a Program that asks for an integer and determine whether it is even or odd. Tip: use the modulo operator (remainder of the division).

value = int(input('Value: '))

if value == 0:
    print(f'{value} is null')
elif value % 2 == 0:
    print(f'{value} is even')
else:
    print(f'{value} is odd')
