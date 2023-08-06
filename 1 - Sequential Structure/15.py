"""
Make a program that asks how much you earn per hour and the number of hours worked in the month.
Calculate and show the total of your salary in that month, knowing that 11% are discounted for Income Tax, 8% for Social Security (INSS, in Portuguese) and 5% for the union, make a program that gives us:
gross salary.
how much you paid to the INSS.
how much you paid to the union.
the net salary.
calculate the discounts and the net salary, according to the table below:

 
-----------------------
+ Gross Salary : $
- IR (11%) : $
- INSS (8%) : $
- Union (5%) : $
= Net Salary : $
------------------------
"""

earnPerH = float(input("How much do you earn per hour?: "))
hoursW = int(input("How many hours worked this month?: "))

monthlySalary = earnPerH * hoursW

IR = (11*monthlySalary) / 100
INSS = (8*monthlySalary) / 100
union = (5*monthlySalary) / 100
net = monthlySalary - (IR + INSS + union)


print("      Table")
print("-----------------------")
print("+ Gross salary: $", monthlySalary)
print("- IR (11%): $", IR)
print("- INSS (8%): $", INSS)
print("- Union (5%): $", union)
print("= Net: $", net)
print("-----------------------")
