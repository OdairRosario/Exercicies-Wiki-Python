# Create a program that reads 2 numbers and then asks the user what operation they want to perform. 
# The result of the operation should be followed by a sentence that states whether the number is:
# even or odd;
# positive or negative;
# integer or decimal.

num1 = float(input('Value1: '))
num2 = float(input('Value2: '))
x = float(0)

operation = input('M-multiplication\nD-division\nA-addition\nS-subtraction:').upper()

if operation == 'M':
    x = num1 * num2
elif operation == 'D':
    x = num1 / num2
elif operation == 'A':
    x = num1 + num2
elif operation == 'S':
    x = num1 - num2

if x != 0:
    if x % 2 == 0:
        final = f'{x} is: even, '
    else: 
        final = f'{x} is: odd, '
    
    if x > 0:
        final += 'positive, '
    else: 
        final += 'negative, '

    if x % 1 == 0:
        final += 'integer'
    else:
        final += 'decimal'
    print(final)
else:
    print('Please, enter the correct input.')
