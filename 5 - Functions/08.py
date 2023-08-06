"""
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
"""

def digitos(n):
    return len(str(n))

n = int(input('Valor: '))

print(f'{digitos(n)} digitos')