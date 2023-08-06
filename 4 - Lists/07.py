"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

vetor = list()
multiplicação = float(1)
soma = float()


for i in range(0,5):
    vetor.append(int(input('Numero: ')))
    multiplicação *= vetor[i]
    soma += vetor[i]

print(f'Soma e multiplicação entre os valores: {soma}\n Soma: {soma}\nMultiplicação: {multiplicação}')