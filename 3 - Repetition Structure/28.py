"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""
valor = float(0)
media = int(0)

while True:
    CD = int(input('Quantidade de CDS: '))
    if CD <= 0:
        continue
    else:
        break
for i in range(1, CD+1):

    while True:
        preco = float(input(f'CD {i}, Preço R$:'))
        if preco < 0:
            print('VALOR INVALIDO, PREÇO DEVE SER MAIOR QUE 0')
            continue
        else:
            break
    media += preco


print(f'{CD} CDS  Preço total: {media}\nMédia de preço por CD: R${media/CD}')