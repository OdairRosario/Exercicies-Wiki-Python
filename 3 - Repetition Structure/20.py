"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias 
e limitando o fatorial a números inteiros positivos e menores que 16.
"""

import math

x = int(input('Numero: '))

while(x < 0 or x > 16):
    x = int(input('Numero inteiro positivo menor que 16: '))

print(math.factorial(x))