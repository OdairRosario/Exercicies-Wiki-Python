"""
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com 
o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 
Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
"""

nota, media = float(0), float(0)
resposta, opc = str(''), str('')
Maior_Acerto, Menor_Acerto, total_alunos = int(0), int(0), int(0)
fechou = False
while True:
    if fechou == True:
        break
    nota = float(0)
    for i in range(0,10):
        while True:
            resposta = input(f'Questão {i+1}[ A - B - C - D - E ]: ').upper()
            if resposta == 'A' or resposta == 'B' or resposta == 'C' or resposta == 'D' or resposta == 'E':
                break
            else:
                continue

        if i == 0 and resposta == 'A':
            nota += 1
        elif i == 1 and resposta == 'B':
            nota += 1
        elif i == 2 and resposta == 'C':
            nota += 1
        elif i == 3 and resposta == 'D':
            nota += 1
        elif i == 4 and resposta == 'E':
            nota += 1
        elif i == 5 and resposta == 'E':
            nota += 1
        elif i == 6 and resposta == 'D':
            nota += 1
        elif i == 7 and resposta == 'C':
            nota += 1
        elif i == 8 and resposta == 'B':
            nota += 1
        elif i == 9 and resposta == 'A':
            nota += 1

    if media == 0:
        Maior_Acerto = Menor_Acerto = nota
    elif Maior_Acerto < nota:
        Maior_Acerto = nota
    elif Menor_Acerto > nota:
        Menor_Acerto = nota

    media += nota
    total_alunos += 1
    while True: 
        opc = str(input('Digite os dados corretamente -> Continuar[S-sim / N-Não]: '))
        if opc.upper() == 'N':
            fechou = True
            break
        else:
            break
            

print(f'Total de alunos: {total_alunos}, media de nota: {media/total_alunos}\nmaior acerto: {Maior_Acerto}, menor acerto: {Menor_Acerto}')
