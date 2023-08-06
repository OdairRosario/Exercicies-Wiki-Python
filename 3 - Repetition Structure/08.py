"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
soma = float()

for i in range(0,5):
    soma += float(input('Valor: '))

print(f'Soma: {soma} - Média: {soma/5}')
