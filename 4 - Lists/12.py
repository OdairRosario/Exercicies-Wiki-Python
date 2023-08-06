"""
Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
"""

idades, alturas = list(), list()
media = float()
qt = 0
for i in range(0,30):
    print(f'ALUNO {i+1}')
    idades.append(int(input('Idade: ')))
    alturas.append(int(input('Altura[cm]: ')))
    media += alturas[i]

media  = media/30

for i in range(0, 30):
    if idades[i] > 13:
        if alturas[i] < media:
            qt += 1

print(f'{qt} alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos')
