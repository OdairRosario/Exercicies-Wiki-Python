"""
Make a program that calculates the roots of a second degree equation, in the form ax2 + bx + c.
The program should ask for the values of a, b and c and make the consistencies, informing the user in the following situations:
If the user informs the value of A equal to zero, the equation is not of the second degree and the program should not ask for the other values, being closed;
If the calculated delta is negative, the equation does not have real roots. Inform the user and close the program;
If the calculated delta is equal to zero the equation has only one real root; inform the user;
If the delta is positive, the equation has two real roots; inform the user;

"""
# ax2 + bx + c
# x = a*2 + b + c

a = float(input('a: '))
if a == 0:
    print('this is not a second degree equation')
else: 
    b = float(input('b: '))
    c = float(input('c: '))
    delta = b**2 - 4*a*c
    if delta < 0:
        print('the equation does not have real roots')
    elif delta == 0:
        print("There is only one real root, which is", -b/(2*a))
    else:
        print('the equation has two real roots')
        print("Root 1:", (-b+delta**(1/2))/(2*a))
        print("Root 2:", (-b-delta**(1/2))/(2*a))
