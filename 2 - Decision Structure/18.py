# Ask for a date in the format dd/mm/yyyy and determine if it is a valid date.

date = str(input('date in dd-mm-yyyy:'))

# Check if the day is between 1 and 31
if int(date[0:2]) > 0 and int(date[0:2]) <= 31:
    # Check if the month is between 1 and 12 and if the separator is '-'
    if int(date[3:5]) > 0 and int(date[3:5]) <= 12 and date[2] == '-':
        # Check if the year is greater than 0 and if the separator is '-'
        if int(date[6:10]) > 0 and date[5] == '-':
            print('This date is valid!')
        else:
            print('Error! Invalid date format')
    else:
        print('Error! Invalid date format')
else:
    print('Error! Invalid date format')
