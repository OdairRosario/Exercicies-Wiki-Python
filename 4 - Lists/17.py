"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
O resultado do atleta será determinado pela média dos cinco valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta
em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser 
encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""
atletas = list()
distancia = list()
ordinais = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
media = float()
contador = int(0)
while True:
    atletas.append(input('Atleta: '))
    if atletas[contador] == ' ' or len(atletas[contador]) == 0:
        atletas.pop(-1)
        break
    else:
        for i in range(0,5):
            x = float(input(f'{ordinais[i]} Salto: '))
            distancia.append(x)
            media += x

        distancia.append(float(media/5))
    print(f'Resultado final\nAtleta: {atletas[-1]}\nSaltos: ')
    for i in distancia[0:4]: print(f'{i} -', end= ' ')
    print(f'\nMedia dos saltos: {distancia[-1]}')
    distancia.clear()
    media = 0
    contador += 1
    