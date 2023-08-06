"""
Faça um programa, com uma função que necessite de um argumento. 
A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""

def PorB(x):
    if x < 0: return 'N'
    else: return 'P'

print(PorB(-19))