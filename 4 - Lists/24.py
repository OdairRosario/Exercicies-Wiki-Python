"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor.
Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para
gerar numeros aleatórios, simulando os lançamentos dos dados.
"""
from random import *
vetor = [0,0,0,0,0,0]

for i in range(0,100):
    x = randint(1,6)
    vetor[x-1] += 1
for i, j in enumerate(vetor):
    print(f'{i+1}  - {j} vezes')