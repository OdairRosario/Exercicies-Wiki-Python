"""
Faça um Programa que peça as quatro notas de 10 alunos,
calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
"""

media = list()
for i in range(0,10):
    nota = float(0)
    print(f'\nAluno {i+1}')
    for j in range(0,4):
        nota += float(input(f'Nota {i+1}:'))
    media.append(nota/4)

for i in media:
    if i >= 7:
        pass
    else:
        media.remove(i)
print('Numero de Alunos com media >= 7: ',len(media))