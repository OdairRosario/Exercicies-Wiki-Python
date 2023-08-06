# Create a Program to read three partial grades of a student. 
# The program should calculate the average obtained by the student and present:
# The message "Approved", if the average is greater or equal to 7, with the respective achieved average;
# The message "Failed", if the average is less than 7, with the respective achieved average;
# The message "Approved with Distinction", if the average is equal to 10.

grade1 = float(input('grade1: '))
grade2 = float(input('grade2: '))
grade3 = float(input('grade3: '))

average = (grade1 + grade2 + grade3) / 3

if average == 10:
    print('Approved with distinction')
elif average >= 7 and average < 10:
    print('Approved')
else: 
    print('Failed')
