"""
The Tabajara Hypermarket is having a meat promotion that you can't miss. Check it out:
                    Up to 5 Kg           Above 5 Kg
Double Filet    $ 4.90 per Kg          $ 5.80 per Kg
Rump            $ 5.90 per Kg          $ 6.80 per Kg
Picanha         $ 6.90 per Kg          $ 7.80 per Kg
To serve all customers, each customer can only take one type of meat from the promotion,
however there are no limits to the amount of meat per customer. If the purchase is made on the Tabajara card, 
the customer will also receive a 5% discount on the total purchase. Write a program that asks for the 
type and quantity of meat bought by the user and generates a receipt, containing the purchase information: 
type and quantity of meat, total price, type of payment, discount amount and amount to pay.
"""

print('Double Filet[F] - Rump[A] - Picanha[P]: ')
type = input('Which meat: ').upper()
quantity = float(input('How many Kg: '))
card = int(input('On the Tabajara card?[0-No,1-Yes]:'))

if type == 'F':
    if quantity <= 5 and quantity > 0:
        x = 4.90
        value = quantity * x
    else:
        x = 5.80
        value = quantity * x
    type = 'Double Filet'
elif type == 'A':
    if quantity <= 5:
        x = 5.90
        value = quantity * x
    else:
        x = 6.80
        value = quantity * x
    type = 'Rump'
elif type == 'P':
    if quantity <= 5:
        x = 6.90
        value = quantity * x
    else:
        x = 7.80
        value = quantity * x
    type = 'Picanha'
else:
    print('Enter the data correctly')

if card == 1:
    value = value - ((value /100)*5)
    payment = 'Tabajara Card'
    discount = int(5)
else:
    payment = 'Cash'
    discount = int(0)

# value of X is the price per kilo
print('\n---- RECEIPT ----\n')
print(f'type: {type}\nquantity: {quantity}Kg\ntotal value: ${quantity*x}\nPayment: {payment}\nDiscount: {discount}\nPrice: ${value}')
