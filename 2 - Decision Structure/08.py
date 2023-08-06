# Make a program that asks the price of three products and informs which product you should buy, knowing that the decision is always for the cheapest one.

prod1 = float(input("Price: "))
prod2 = float(input("Price: "))
prod3 = float(input("Price: "))

if prod1 < prod2:
    if prod1 < prod3:
        print(f"Product 1 is the cheapest: ${prod1}")
    else:
        print(f"Product 3 is the cheapest: ${prod3}")
else:
    if prod2 < prod3:
        print(f"Product 2 is the cheapest: ${prod2}")
    else:
        print(f"Product 3 is the cheapest: ${prod3}")
