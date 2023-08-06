"""
Make a program for the calculation of a payroll, knowing that the deductions are from Income Tax, which depends on the gross salary
(according to the table below) and 3% for the Union and that the FGTS corresponds to 11% of the Gross Salary, but it is not deducted (it is the company that deposits).
Net Salary corresponds to Gross Salary minus deductions. The program should ask the user for the value of their hour and the number of hours worked in the month.
IR Discount:
Gross Salary up to 900 (inclusive) - exempt
Gross Salary up to 1500 (inclusive) - 5% discount
Gross Salary up to 2500 (inclusive) - 10% discount
Gross Salary above 2500 - 20% discount Print the information on the screen, arranged according to the example below.

In the example the hour value is 5 and the amount of hour is 220.

 Gross Salary: (5 * 220)        : $ 1100.00
        (-) IR (5%)                     : $   55.00  
        (-) INSS ( 10%)                 : $  110.00
        FGTS (11%)                      : $  121.00
        Total deductions              : $  165.00
        Net Salary                 : $  935.00
        
"""

hour = float(input("How much do you earn per Hour: "))
m_hours = int(input("How many hours did you work in the month: "))

salary = hour * m_hours
print(f"\n Gross : ${salary}")

if salary <= 900 and salary > 0:
    print('IR(exempt) : $0.00')
elif  salary <= 1500:
    IR = ((5 * salary) / 100)
    print('IR(5%) : $', IR)
elif salary  <= 2500:
    IR = ((10 * salary)/100)
    print('IR(10%) : $', IR)
elif salary > 2500:
    IR = ((20 * salary)/100)
    print('IR(20%) : $', IR)
else:
    print('something wrong happened')
    
net_salary = salary - (((10 * salary)/100) + IR)
print('INSS(10%) : $', ((10 * salary)/100))
print('deductions : $', ((10 * salary)/100) + IR)
print('net : $', net_salary)
