"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o 
número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""

populacaoA = float(80000)
populacaoB = float(200000)
anos = int(0)
while(populacaoA < populacaoB):
    populacaoA += ((populacaoA/100)* 3) 
    populacaoB += ((populacaoB/100) * 1.5)
    anos += 1

print('Para que a população A passe a B são nescessarios {} anos\nPopulação A: {} População B: {}'.format(anos,populacaoA,populacaoB))
