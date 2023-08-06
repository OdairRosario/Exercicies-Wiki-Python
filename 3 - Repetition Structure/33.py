"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as
um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, 
bem como a média das temperaturas.
"""

temperatura = int()
media = float()
maior = int(0)
menor = int(0)
i = int(1)

while(True):
    temperatura = int(input('Temperatura[000 encerra]: '))
    media += temperatura
    if str(temperatura) == str(000):
        break
    if i == 1:
        maior = temperatura
        menor = temperatura
    else:
        if temperatura > maior:
            maior = temperatura
        if temperatura < menor:
            menor = temperatura

    i += 1

print(f'Menor: {menor}\nmaior: {maior}\nmedia: {media/i}')