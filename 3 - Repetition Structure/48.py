"""
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
"""
numero = str(input('Numero: '))
saida = str('')

for i in range(len(numero)-1, -1, -1 ):
    saida += numero[i]

print(f'=> {saida}')