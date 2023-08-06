# Make a Program that reads a number and displays the corresponding day of the week.
# (1-Sunday, 2- Monday, etc.), if you type another value it should appear invalid value.

day = int(input("Value: "))

if day == 1:
    print('Sunday')
elif day == 2:
    print('Monday')
elif day == 3:
    print('Tuesday')
elif day == 4:
    print('Wednesday')
elif day == 5:
    print('Thursday')
elif day == 6:
    print('Friday')
elif day == 7:
    print('Saturday')
else:
    print('Invalid value')
