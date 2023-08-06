"""
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
"""

N = int(input('N: '))

H = int(1)

for i in range(0,N):
    H += 1/N

print(f'Valor de H: {H:.2f}')