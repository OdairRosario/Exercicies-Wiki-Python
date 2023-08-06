"""
Make a program that reads the two partial grades obtained by a student in a discipline over a semester, and calculate his average.
The assignment of concepts follows the table below:

 Average Achievement  Concept
 Between 9.0 and 10.0        A
 Between 7.5 and 9.0         B
 Between 6.0 and 7.5         C
 Between 4.0 and 6.0         D
 Between 4.0 and zero        E
The algorithm should show on the screen the grades, the average, the corresponding concept and the message “APPROVED” if the concept is A, B or C or “FAILED” if
the concept is D or E.
"""

grade1 = int(input('grade1: '))
grade2 = int(input('grade2: '))


average = (grade1 + grade2)/ 2
print(f'average: {average}')
    
concept = str()
status = str()

if average >= 9 and average <= 10:
    concept = 'A'
    status = 'APPROVED'
    
if average < 9 and  average >= 7.5 :
    concept = 'B'
    status  = 'APPROVED'
    
if average < 7.5 and average >= 6:
    concept = 'C'
    status = 'APPROVED'

if average >=  4 and average < 6:
    concept = 'D'
    status = 'FAILED'
if average < 4:
    concept = 'E'
    status = 'FAILED'

print(f'Status: {status}\nConcept: {concept}')

