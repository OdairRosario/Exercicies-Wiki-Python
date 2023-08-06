"""
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
"""

def reverso(n):
    x = str()
    n = str(n)
    for i in range(len(n), 0, -1):
        x += f'{n[i-1]}'
    return x
n = int(input('N: '))

print(reverso(n))