#Make a Program that asks for a number corresponding to a certain year and then informs if this year is a leap year or not.
year = int(input('Enter a year: '))

if year % 4 == 0:
    print(f'The year {year} is a leap year')
else:
    print('This year is not a leap year')
