"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
"""

vetorA = list()
soma = float()

for i in range(0,10):
    vetorA.append(float(input('Numero: ')))

for i in vetorA:
    soma += i**2

print(f'Soma do quadrado dos valores: {soma}')