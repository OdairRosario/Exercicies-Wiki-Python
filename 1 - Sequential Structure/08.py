# Make a Program that asks how much you earn per hour and the number of hours worked in the month. Calculate and show the total of your salary in that month.

earnPerHour = float(input("How much do you earn per hour? :"))
workedHours = int(input("How many hours have you worked this month? "))

earningsPerMonth = earnPerHour * workedHours

print(f"You worked {workedHours}h this month, and earned $ {earningsPerMonth}")
