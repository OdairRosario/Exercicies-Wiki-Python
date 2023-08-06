"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""

candidato1 = int(0)
candidato2 = int(0)
candidato3 = int(0)
voto = int(0)
eleitores = int(0)

while(eleitores <= 0): eleitores = int(input('Quantos eleitoes?[maior que 0]:'))

for i in range(0, eleitores):
    voto = int(input('candidato A[1], candidato B[2], candidato C[3]\nvoto:'))
    if voto > 3 or voto <= 0:
        while(voto > 3 or voto <= 0): voto = int(input('VOTO INVALIDO!\ncandidato A[1], candidato B[2], candidato C[3]\nvoto:'))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1

print(f'{eleitores} Votantes.\ncandidato A: {candidato1} votos\ncandidato B: {candidato2} votos\ncandidato C: {candidato3} votos')

