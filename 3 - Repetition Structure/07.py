"""
Faça um programa que leia 5 números e informe o maior número.
"""

maior = float(0)

for i in range(0,5):
    num = float(input('Valor: '))
    if i == 0:
        maior == num
    elif num > maior:
        maior = num
    
print(f'Maior numero: {maior}')