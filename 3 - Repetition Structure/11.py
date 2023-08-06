"""
Altere o programa anterior para mostrar no final a soma dos números.
"""

x = int(input('Valor1: '))
y = int(input('Valor2: ')) + 1
soma = int(0)

for i in range(x, y):
    print(i, end=' ')
    soma += i

print(f'Soma entre todos: {soma}')
