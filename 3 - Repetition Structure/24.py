"""
Faça um programa que calcule o mostre a média aritmética de N notas
"""

num = int(input('Quantidade de notas: ')) + 1
media = float(0)
for i in range(1,num):
    x = int(input('Nota: '))
    media += x
print(f'média: {media/i} das {i} notas lidas')