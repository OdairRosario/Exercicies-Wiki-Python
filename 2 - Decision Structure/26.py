"""
A gas station is selling fuel with the following discount table:
Alcohol:
up to 20 liters, 3% discount per liter
over 20 liters, 5% discount per liter
Gasoline:
up to 20 liters, 4% discount per liter
over 20 liters, 6% discount per liter
Write an algorithm that reads the number of liters sold, the type of fuel 
(encoded as follows: A-alcohol, G-gasoline), calculate and print the amount to be paid by the customer knowing 
that the price per liter of gasoline is $ 2.50 the price per liter of alcohol is $ 1.90.
"""

liter = float(input("Liters: "))
type = input('G- Gasoline or A-Alcohol: ').upper()
gasoline = float(2.5)
alcohol = float(1.90)

if type == 'G':
    if liter <= 20 and liter > 0:
        price = liter * (gasoline - (gasoline/100)*4) 
    if liter > 20:
        price = liter * (gasoline  - (gasoline/100)*6) 
    print(f'Price: {price} for {liter} liters')
elif type == 'A':
    if liter <= 20 and liter > 0:
        price = liter * (alcohol - (alcohol/100)*3)
    if liter > 20:
        price = liter * (alcohol -  (alcohol/100)*5)
    print(f'Price: {price} for {liter} liters')
else:
    print('Please, enter the data correctly.')
