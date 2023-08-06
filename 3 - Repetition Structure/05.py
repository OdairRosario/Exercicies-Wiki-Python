"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.
"""


while(1):
    anos = int(0)
    
    PopulacaoA = float(input('População A: '))
    taxaA = float(input('Taxa %A: '))
    while (taxaA <= 0):
        taxaA = float(input('Taxa maior que 0\nTaxa %A: '))

    PopulacaoB = float(input('População B: '))
    taxaB = float(input('Taxa %B: '))
    while(taxaB <= 0):
        taxaB = float(input('taxa maior que 0\nTaxa %A'))
    

    while(PopulacaoA < PopulacaoB):
        PopulacaoA += ((PopulacaoA / 100)*taxaA)
        PopulacaoB += ((PopulacaoB / 100)*taxaB)
        anos += 1
    print(f'{anos} anos para população A passar população B')

    if int(input('Executar novamente[1- sim/0- não]: ')) == 0:
        break
        