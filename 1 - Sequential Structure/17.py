"""
Make a program for a paint store. The program should ask for the size in square meters of the area to be painted.
Consider that the paint coverage is 1 liter for every 6 square meters,
and that the paint is sold in 18-liter cans, which cost $ 80.00, or in 3.6-liter gallons, which cost $ 25.00.
Inform the user the quantities of paint to be purchased and their respective prices in 3 situations:
buy only 18-liter cans;
buy only 3.6-liter gallons;
mix cans and gallons, so that the waste of paint is smaller.
Add 10% slack and always round up the values, that is, consider full cans.
"""

import math
size = float(input("How many square meters is the area to be painted: ")) #109

Liter = float(6)
Can = 80 #price

gallon = 25 #price

can_qt = math.ceil(size / (Liter*18))
can_pr = can_qt * Can
print("Buying only 18-liter cans: $", can_pr)
print("Quantity of cans to be purchased: ", can_qt)

gallon_qt = math.ceil(size / (Liter*3.6))
gallon_pr = gallon_qt * gallon
print("\nBuying only 3.6-liter gallons: $", gallon_pr)
print("Quantity of gallons to be purchased: ", gallon_qt)

can_qt = math.floor(size / (Liter * 18))
can_pr = can_qt*80

size -= can_qt*(Liter*18)

gallon_qt = math.ceil(size / (Liter*3.6))
gallon_pr = gallon_qt * 25
print(f"\nMixing between gallons and cans: $", gallon_pr+can_pr)
print(f"Cans: {can_qt} and gallons: {gallon_qt}")
