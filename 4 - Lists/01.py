"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""

vetor = list()
for i in range(0,5):
    vetor.append( int(input('Numero: ')))
for i in vetor:
    print(i, end=' ')