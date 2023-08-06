"""
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
"""

voto_nulo, voto_branco, voto, total = int(0), int(0), int(0), int(0)
procentagenVN, porcetagenVB = float(0), float(0)
candidato1, candidato2, candidato3, candidato4 = int(0), int(0), int(0), int(0)
while True:
    print('1 - João / 2 - Odair / 3 - Sandro / 4 - Ruan / 5 - Nulo / 6 - Branco')
    voto = int(input('voto[0-encerra]: '))
    total += 1
    if voto == 0: break
    elif voto == 1: candidato1 += 1
    elif voto == 2: candidato2 += 1
    elif voto == 3: candidato3 += 1
    elif voto == 4: candidato4 += 1
    elif voto == 5: voto_nulo += 1
    elif voto == 6: voto_branco += 1
    else: 
        while voto < 0 or voto > 6:
            voto = int(input('Valor invalido\nvoto[0-encerra]: '))
    
print(f'candidato 1: {candidato1}\ncandidato 2: {candidato2}\ncandidato 3: {candidato3}\ncandidato 4: {candidato4}\nvoto nulo: {voto_nulo}\nvoto em branco: {voto_branco}')

pocentagenVN = float(((voto_nulo / total) * 100))# erro aqui.
porcetagenVB = float(((voto_branco / total) * 100))
print(f'% de votos nulos: {procentagenVN}\n % de votos brancos: {porcetagenVB:.2f}')

"""
pc   voto
100   101
x      17

101x = 100*17
x = 100*17/101
"""