# Create a Program that asks for a number and informs whether the number is an integer or decimal. Tip: use a rounding function.

import math

number = float(input('Value: '))

if number % 1 == 0:
    print(f'{number} is an integer.')
else:
    print(f'{number} is a decimal.')
