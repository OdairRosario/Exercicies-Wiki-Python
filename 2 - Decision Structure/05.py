"""
Make a program for reading two partial grades of a student. The program should calculate the average achieved by the student and present:
The message "Approved", if the achieved average is greater than or equal to seven;
The message "Failed", if the average is less than seven;
The message "Approved with Distinction", if the average is equal to ten.
"""

grade1 = float(input("Enter grade1: "))
grade2 = float(input("Enter grade2: "))

average = (grade1 + grade2) / 2

if average == 10:
    print("Approved with distinction")
elif average < 7:
    print('Failed')
else:
    print("Approved")
