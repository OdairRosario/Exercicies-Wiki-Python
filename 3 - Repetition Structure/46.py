"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta,
o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer 
um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos 
conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). O programa deve ser encerrado
quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m
#29.5/5

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
""" 

nome, NomeMelhor = str(''), str()
distancia, media, melhorMedia = float(), float(), float()
melhorSalto, PiorSalto = float(), float()
j = int()

while True:
    j += 1
    media = 0
    
    nome = str(input('Atleta[Não informar encerra]: '))
    if nome == '' or nome == ' ':
        break
    for i in range(0,5):
        if i == 0:
            melhorSalto = PiorSalto = distancia 
            distancia = float(input('Primeiro salto: '))
        if i == 1: distancia = float(input('Segundo salto: '))
        if i == 2: distancia = float(input('Terceiro salto: '))
        if i == 3: distancia = float(input('Quarto salto: '))
        if i == 4: distancia = float(input('Quinto salto: '))

        if distancia > melhorSalto: melhorSalto = distancia
        if PiorSalto > distancia : PiorSalto = distancia

        media += distancia

    if j == 1:
        melhorMedia = media
        NomeMelhor = nome
    if melhorMedia < media: 
        melhorMedia = media
        NomeMelhor = nome
    
    media = media/5
    print(f'Melho salto: {melhorSalto}\nPior salto{PiorSalto}\nMedia dos demais saltos: {media:.2f}')
print(f'Resultado final:\n{NomeMelhor}: {melhorMedia:.2f}')