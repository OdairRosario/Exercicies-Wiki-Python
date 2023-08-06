"""
Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘|‘.
Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo
igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para
valores dentro da faixa de forma elegante.
"""

def moldura(linhas,colunas):
    if linhas > 20: linhas = 20
    if linhas < 0: linhas = 1
    if colunas > 20:colunas = 20
    if colunas < 0: colunas = 1

    print('+ ' + ' − '*colunas + ' +')
    for i in range(0,linhas):
        print('| ' + '   '*colunas + ' |')
    print('+ ' + ' − '*colunas + ' +')

linha = int(input('Linhas[20=max]: '))
coluna = int(input('Colunas[20=max]: '))

moldura(linha,coluna)