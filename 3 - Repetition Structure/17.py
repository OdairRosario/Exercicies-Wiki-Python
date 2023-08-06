"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""

num = int(input('Valor: '))

for i in range(num-1, 0, -1):
    num = num * i

print(num)