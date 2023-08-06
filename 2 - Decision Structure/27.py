"""
A fruit store is selling fruits with the following price table:
                    Up to 5 Kg           Above 5 Kg
Strawberry       $ 2.50 per Kg         $ 2.20 per Kg
Apple             $ 1.80 per Kg         $ 1.50 per Kg
If the customer buys more than 8 Kg of fruit or the total purchase amount exceeds $ 25.00, they will also receive a 10% discount on this total. 
Make an algorithm to read the quantity (in Kg) of strawberries and the quantity (in Kg) of apples purchased and write the amount to be paid by the customer.
"""

strawberry = float(input('Strawberry Kg:'))
apple = float(input('Apple Kg:'))

if strawberry <= 5:
    if (strawberry + apple) > 8:
        price =  (strawberry * 2.5) - (((strawberry * 2.5) / 100) * 10)
        print(f'Strawberry: {strawberry}Kg Price: ${price}')
    else:
        price = (strawberry * 2.5)
        print(f'Strawberry: {strawberry}Kg Price: ${price}')
if strawberry > 5:
    if (strawberry + apple) > 8:
        price = (strawberry * 2.20) - (((strawberry * 2.20) / 100) * 10)
        print(f'Strawberry: {strawberry}Kg Price: ${price}')
    else:
        price = strawberry * 2.20
        print(f'Strawberry: {strawberry}Kg Price: ${price}')
        
if apple <= 5:
    if (strawberry + apple) > 8:
        price = (apple * 1.8) - (((apple * 1.8) / 100)* 10) 
        print(f'Apple: {apple}Kg Price: ${price}')
    else:
        price = apple * 1.8
        print(f'Apple: {apple}Kg Price: ${price}')
if apple > 5:
    if (strawberry + apple) > 8:
        price = (apple * 1.5) - (((apple * 1.5) / 100) * 10)
        print(f'Apple: {apple}Kg Price: ${price}')
    else:
        price = apple * 1.5
        print(f'Apple: {apple}Kg Price: ${price}')
