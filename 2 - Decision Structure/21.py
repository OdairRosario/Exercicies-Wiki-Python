"""
Create a Program for an ATM. The program should ask the user the withdrawal amount and then inform how many notes of each value will be provided. 
The available notes will be 1, 5, 10, 50 and 100 reais. The minimum amount is 10 reais and the maximum is 600 reais.
The program should not worry about the number of notes available in the machine.
Example 1: To withdraw the amount of 256 reais, the program provides two 100 reais notes, one 50 reais note, one 5 reais note and one 1 real note;
Example 2: To withdraw the amount of 399 reais, the program provides three 100 reais notes, one 50 reais note, four 10 reais notes, 
one 5 reais note and four 1 real notes.
"""
import math
withdraw = float(input('Withdraw amount: '))
x = withdraw
if withdraw  < 10 or withdraw > 600: 
    print('The minimum and maximum amount for withdrawal is 10 and 600 reais')
else: 
    hundred = fifty = ten = five = one = int(0)
    if withdraw >= 100:
        hundred = math.floor(withdraw / 100)# current withdrawal / note value = number of notes.
        withdraw = withdraw - (hundred * 100)

    if withdraw >= 50:
        fifty = math.floor(withdraw/50)
        withdraw = withdraw - (fifty * 50)
    if withdraw >= 10:
        ten = math.floor(withdraw/10)
        withdraw = withdraw - (ten*10)
    if withdraw >= 5:
        five = math.floor(withdraw/5)
        withdraw = withdraw - (five*5)
    if withdraw >= 1:
        one = math.ceil(withdraw/1)
        withdraw = withdraw - (one* 1)

    print(f'Withdraw amount: R${x}')
    if hundred >= 1:
        print(f'100 real notes: {hundred}')
    if fifty >= 1:
        print(f'50 real notes: {fifty}')
    if ten >= 1: 
        print(f'10 real notes: {ten}')
    if five >= 1:
        print(f'5 real notes: {five}')
    if one >= 1:
        print(f'1 real notes: {one}')
