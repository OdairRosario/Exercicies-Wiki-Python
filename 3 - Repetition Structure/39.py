"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro 
representando o número do aluno e o segundo representando a sua altura em centímetros.
Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
"""

mb_aluno, mb_altura = int(), int()
ma_aluno, ma_altura = int(), int()
for i in range(1,11):
    numero = int(input(f'Numero aluno {i}: '))
    altura = int(input('Altura[Cm]: '))
    while altura <= 0: altura = int(input('DADOS INVALIDOS, DEVE SER MAIOR QUE 0\nAltura[Cm]: '))
    if i == 1:
        ma_aluno = mb_aluno = numero
        ma_altura = mb_altura = altura
    else:
        if altura < mb_altura:
            mb_altura = altura
            mb_aluno = numero
        if altura > ma_altura:
            ma_altura = altura
            ma_aluno = numero
print(f'aluno mais baixo -> {mb_aluno} com {mb_altura}cm')
print(f'aluno mais alto -> {ma_aluno} com {ma_altura}cm')
