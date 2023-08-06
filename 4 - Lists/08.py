"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
"""

idade, altura = list(), list()

for i in range(0,5):
    idade.append(input('Idade: '))
    altura.append(input('Altura: '))
for i in range(4,-1,-1):
    print(f'Idade: {idade[i]}, Altura: {altura[i]}')