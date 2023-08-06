"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""

temperaturaMedia = list()
meses = ['Janeiro', 'Feveireiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
media = float()
for i in range(0,12):
    temperaturaMedia.append(float(input(f'Temperatura media[{meses[i]}]: ')))

for i in temperaturaMedia:
    media += i
media = media /12

for i in range(0,12):
    if temperaturaMedia[i] > media:
        print(f'{temperaturaMedia[i]} no mês {meses[i]}')
