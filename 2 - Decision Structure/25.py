"""
Make a program that asks a person 5 questions about a crime. The questions are:
"Did you call the victim?"
"Were you at the crime scene?"
"Do you live near the victim?"
"Did you owe the victim?"
"Have you ever worked with the victim?" 
The program should, in the end, issue a classification about the person's involvement in the crime. 
If the person answers 2 questions positively, they should be classified as "Suspect", between 3 and 4 as "Accomplice", and 5 as "Murderer".
Otherwise, they will be classified as "Innocent".
"""

question1 = input('Did you call the victim?[Y-yes/N-no]: ').upper()
question2 = input('Were you at the crime scene?[Y-yes/N-no]: ').upper()
question3 = input('Do you live near the victim?[Y-yes/N-no]: ').upper()
question4 = input('Did you owe the victim?[Y-yes/N-no]: ').upper()
question5 = input('Have you ever worked with the victim?[Y-yes/N-no]: ').upper()

Yes = int(0)

if question1[0] == 'Y': Yes += 1
if question2[0] == 'Y': Yes += 1
if question3[0] == 'Y': Yes += 1
if question4[0] == 'Y': Yes += 1
if question5[0] == 'Y': Yes += 1

if Yes == 2:
    print('Classification: Suspect')
elif Yes == 3 or Yes == 4:
    print('Classification: Accomplice')
elif Yes == 5:
    print('Classification: Murderer')
else:
    print('Classification: Innocent')
