"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""

par = int()
impar = int()
num = int()
for i in range(0,10):
    num = int(input('Valor: '))

    if num % 2 == 0:
        par = int(par + 1)
    else:
        impar = int(impar + 1)

print(f'Impares: {impar}\n Pares: {par}')