"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""
maior, menor = 0,0

ler = int(input('Quantidade de numeros: '))

for i in range(0,ler):
    x = float(input('Valor: '))
    if i == 0:
        maior  = menor = x
    else:
        if x > maior:
            maior = x
        elif x < menor:
            menor = x
        else:
            pass

print(f'Numeros pedidos: {ler}\nMaior: {maior}\nMenor: {menor}')