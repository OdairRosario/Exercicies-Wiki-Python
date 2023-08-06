"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""

Par = list()
Impar = list()
x = list()
for i in range(0,20):
    x.append(int(input('Numero: ')))
    if x[i]%2 == 0:
        Par.append(x[i])
    else:
        Impar.append(x[i])

print(f'Pares: {Par}\nImpares: {Impar}\nNumeros lidos: {x}')