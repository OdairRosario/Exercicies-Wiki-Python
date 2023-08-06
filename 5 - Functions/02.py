"""
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
"""

def emprime(n):
    sr = str()
    for i in range(1,n+1):
        sr += f'{i} '
        print(sr)

n = int(input('N: '))

emprime(n)