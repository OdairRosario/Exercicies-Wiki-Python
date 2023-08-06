"""
Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
"""

turmas = int(input('Turmas: '))
alunos = int(0)
media = float(0)
while turmas <= 0: turmas = int(input('VALORES INVALIDOS!\nTurmas[maior que 0]: '))

for i in range(1,turmas+1):
    alunos = int(input(f'Turma {i}, alunos[maior que 0 e menor que 40]: '))
    while(True): 
        if alunos < 40 and alunos > 0: 
            break 
        else: 
            alunos = int(input(f'VALORES INVALIDOS!\nTurma {i}, alunos[maior que 0 e menor que 40]: '))
    media += alunos

media = int(media / turmas)
print(f'{turmas} turmas\n{media} alunos em media por turma')