"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

vetor = list()

for i in range(0,10):
    vetor.append(input('Numero: '))
for i in range(9,-1,-1):
    print(vetor[i], end=' ')