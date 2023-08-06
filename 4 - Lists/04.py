"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

vetor = list()
vogais = ['A', 'E', 'I', 'O', 'U']
consoantes = list()
for i in range(0,10):
    vetor.append(input('Letra: ').upper())
    if vetor[i] not in vogais:
       pass
    else:
       consoantes.append(vetor[i])

for i in consoantes:
    print(i, end = ' ')
