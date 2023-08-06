""" 
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!

pronto refatorar agora!
"""
def removeQuebra(lista):
    for i, j in enumerate(lista):
        lista[i]  = j[0:len(j)-1]
    return lista

from random import *
palavras = list(open('11Palavras.txt', 'r'))
palavras = removeQuebra(palavras)
palavra = palavras[randrange(0,len(palavras))].lower()
print(palavra)
palavraF = list(len(palavra) * '_')
letra = str()

erros = int()
while True:
    palavraV = str()
    letra = input('\nDigite uma letra: ').lower()
    if letra not in palavra:
        erros+= 1
        if erros == 5:
            print('Você foi enforcado e perdeu o jogo')
            break
        else:
            print(f'-> Você errou pela {erros}ª vez. Tente de novo!')
    else:
        for i,j in enumerate(palavra):
            if j == letra:
                palavraF[i] = j

        for i in palavraF: palavraV += i
        if palavraV == palavra:
            p = str()
            for i in palavraV: p +=i
            print(f'A palavra é: {p}')
            
            print('Você ganhou!')
            break
        print('A palavra é: ', end = '')
        for i in palavraV: print(f' {i} ',end = '')