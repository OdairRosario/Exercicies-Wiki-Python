"""
Create a program that reads an integer less than 1000 and prints the number of hundreds, tens and units of the same.
Observe the terms in the plural, the placement of "and", the comma among others. Example:
326 = 3 hundreds, 2 tens and 6 units
12 = 1 ten and 2 units Test with: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 and 16
"""

number = int(input('value < 1000:'))

if number >= 1000:
    print("Enter a value less than a Thousand")
else:
    number = str(number)
    pos = len(number)
    if pos == 3:
        if number[0] == '1':
            print('hundred: ',number[0])
        else:
            print('hundreds: ',number[0])

        if number[1] == '1':
            print('ten: ', number[1])
        else:
            print('tens', number[1])

        if number[2] == '1' :
            print('unit', number[2])
        else:
            print('units', number[2])
            
    elif pos == 2:
        if number[0] == '1':
            print('ten: ', number[0])
        else:
            print('tens', number[0])

        if number[1] == '1' :
            print('unit', number[1])
        else:
            print('units', number[1])
    elif pos == 1:
        
        if number[0] == '1' :
            print('unit', number[0])
        else:
            print('units', number[0])
