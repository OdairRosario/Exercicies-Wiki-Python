"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
 
vetor = list()
media = 0
for i in range(0,4):
    vetor.append(int(input('numero: ')))

for i in vetor:
    media += i

print(f'media: {media/len(vetor)} dos numeros: {vetor}')