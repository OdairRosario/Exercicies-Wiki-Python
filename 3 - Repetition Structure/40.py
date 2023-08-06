"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence; [x]
Qual a média de veículos nas cinco cidades juntas; [x]
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio. [x]
"""
MenorIndice = int()
MenorIndiceCodigo = int()

MaiorIndice = int()
MaiorIndiceCodigo = int()

mediaVeiculos = float()
mediaAcidentes = float()

j = int(0)

for i in range(1,6):
    codigo = int(input('Codigo da cidade: '))
    veiculos = int(input('Numero de veiculos: '))
    acidentes = int(input('Numero de acidentes: '))
    if veiculos < 2000:
        mediaAcidentes += acidentes
        j+= 1
    if i == 1:
        MenorIndice = MaiorIndice = acidentes
        MenorIndiceCodigo = MaiorIndiceCodigo = codigo
    else:
        if MenorIndice > acidentes:
            MenorIndice = acidentes
            MenorIndiceCodigo = codigo
        if MaiorIndice < acidentes:
            MaiorIndice = acidentes
            MaiorIndiceCodigo = codigo
    mediaVeiculos += veiculos

print(f'Menor indice -> {MenorIndice} na cidade de codigo -> {MenorIndiceCodigo}')
print(f'Maior indice -> {MaiorIndice} na cidade de codigo -> {MaiorIndiceCodigo}')
print(f'Media de veiculos nas {i} cidades -> {mediaVeiculos/i}')
print(f'Media de acidentes em cidades com menos de 2000 veiculos ->{mediaAcidentes/j}')