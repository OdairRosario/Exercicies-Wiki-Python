"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""


num = int(input("Valor:: "))
k = 2
while k < num:
    if num % k == 0:
        print (num, "não é primo.")
        k = num
    k += 1
if k == num:
    print (num, "é primo.")

if num == 1:
    print (num, "é primo.")
            