"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
"""

import math
numero = int(input('Fatorial de: '))
saida = str(f'{numero}! = ')

for i in range(numero,1, -1):
    saida += f'{i} . '

saida += f'1 = {math.factorial(numero)}'

print(saida)