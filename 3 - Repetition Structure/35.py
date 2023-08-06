"""
Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos
números primos existentes entre 1 e um número inteiro informado pelo usuário.
"""

n = int(input('De 0 até que Numero:'))
while n <= 0: n = int(input('[VALOR INVALIDO!]\nDe 0 até que Numero: '))

for i in range(2,n+1):
    if i == 2:
        print(f'{i}',end = ' ')
    if i % i == 0 and i % 1 == 0 and i % 3 != 0 and i % 2 != 0 and i% 5 != 0:
        print(f'{i}', end = ' ')