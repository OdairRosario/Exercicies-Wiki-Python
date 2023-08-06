"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""
x = int(input('Valor1: '))
y = int(input('Valor2: ')) + 1

for i in range(x, y):
    print(i, end=' ')