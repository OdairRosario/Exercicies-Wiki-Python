"""
Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição
e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3,
com números de 1 a 9:
8  3  4   [15]
1  5  9   [15]
6  7  2   [15]
[15] [15] [15]
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.

from random import *

def GeraQuadrados():
    vetor, aux, retorno = list(), list(), list()
    x = str()
    ## Problema com a quantidade de vetores que deverão ser criados
    while True:
        while True:
            x = str(randint(1,10))
            print(len(vetor))
            if x in vetor: continue
            elif len(vetor) == 9: break
            else: vetor.append(x)
        if vetor in retorno:
            continue

        retorno.append(vetor)
    return retorno
def QuadradoMagico():
    pass

print(GeraQuadrados())
"""

  
def geraQuadradoMagico():
    size = 3
    max = size * size
    quadrado = [0] * 3
    for i in range(0, 3):
        quadrado[i] = [0] * 3
    x = 0
    y = 1
    quadrado[x][y] = 1

    for z in range(2, max + 1):
        old_x = x
        old_y = y
        x -= 1
        y += 1

        if (x < 0):
            x = size - 1
        if (y >= size):
            y = 0

        print('%d %d' % (x, y), end= ' ')
        if (quadrado[x][y] == 0):
            quadrado[x][y] = z
        else:
            x = old_x + 1
            y = old_y
            if (x > size):
                x = 0
            quadrado[x][y] = z
    return quadrado


def imprimeQuadrado(quadrado):
    for i in quadrado:
        for j in i:
            print('%d\t' % (j), end = ' ')
        print()

# Funcao principal
quadrado = geraQuadradoMagico()
imprimeQuadrado(quadrado)
