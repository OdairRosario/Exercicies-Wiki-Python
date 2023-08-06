"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. 
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e 
identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar 
o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, 
você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, 
de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá 
ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso 
também deverá ser feito através de uma função, que será chamada pelo programa principal.
"""
arquivo = open('23Usuarios.txt', 'r') 
total = float()
dados = list()
for i in arquivo:
    dados.append(i.split())

with open('23Relatorio.txt', 'w') as arquivo: 
    x = str('------------------------------------------------------------------------\nNr.  Usuario        Espaco utilizado     % do uso\n')
    arquivo.write(x)
    for i in dados: total += float(i[1])
    for i, j in enumerate(dados):
        while len(j[0]) < 15:  
            j[0] += ' '
        j[1] = str(j[1])
        porecentagem = ((float(j[1]) /total) *100)
        x = f'{i+1}   {j[0]}    {float(j[1]) / (1024*1024):.2f} MB          {porecentagem:.2f}%\n'
        arquivo.write(x)
print('Finalizado com secesso!')