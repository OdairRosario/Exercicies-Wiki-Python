"""
Tabajara Organizations have decided to give their employees a raise and hired you to develop the program that will calculate the adjustments.
Make a program that receives the salary of a collaborator and the adjustment according to the following criteria, based on the current salary:
salaries up to $ 280.00 (including) : increase of 20%
salaries between $ 280.00 and $ 700.00 : increase of 15%
salaries between $ 700.00 and $ 1500.00 : increase of 10%
salaries from $ 1500.00 onwards : increase of 5% After the increase is made, report on the screen:
the salary before the adjustment;
the percentage increase applied;
the amount of the increase;
the new salary, after the increase.
"""

salary = float(input("Enter your salary: "))
print(f"Salary before: ${salary}")

if salary < 280 and salary >= 0:
    increase = ((salary * 20) / 100)
    salary = ((salary *120)/ 100)
    print("Increase of: 20%")
    
elif salary >= 280 and salary < 700:
    increase = ((salary * 15) / 100)
    salary = ((salary * 115) / 100)
    print("Increase of: 15%")
    
elif salary >= 700 and salary < 1500:
    increase = ((salary * 10) / 100)
    salary = ((salary * 110) / 100)
    print("Increase of: 10%")
    
elif salary > 1500:
    increase = ((salary * 5)/ 100)
    salary =((salary * 105) / 100)
    print("Increase of: 5%")

else:
    print('There is something wrong')


print(f"Increase amount: ${increase}")
print(f"Salary after: ${salary}")
