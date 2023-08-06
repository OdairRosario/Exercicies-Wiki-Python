"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" 
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
respostas = list()
contador = 0
respostas.append(str(input('Telefonou para vitima?[S-Sim/N-Não]: ')[0].upper()))
respostas.append(str(input('Esteve no local do crime?[S-Sim/N-Não]: ')[0].upper()))
respostas.append(str(input('Mora perto da vitima?[S-Sim/N-Não]: ')[0].upper()))
respostas.append(str(input('Devia para a vitima?[S-Sim]/N-Não]: ')[0].upper()))
respostas.append(str(input('Ja trabalhou com a vitima?[S-Sim/N-Não: ')[0].upper()))

for i in respostas:
    if i == 'S': contador += 1



if contador == 2:
    print('Classificação: Suspeita')
elif contador == 3 or contador == 4:
    print('Classificação: Cumplice')
elif contador == 5:
    print('Classificação: Culpado')
else:
    print('Classificação: Inocente')