"""
Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que
será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto
e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra
deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
"""
from random import randint, choice

def embaralha(palavra):
    retorno = str()
    palavra = list(palavra)
    for i in range(0,len(palavra)):
        letra = choice(palavra)
        palavra.remove(letra)
        retorno += letra
    return retorno

arquivo = open("13Palavras.txt", 'r')
palavras = [linha[:-1] for linha in arquivo]
palavra = palavras[randint(0,len(palavras)-1)]
palavraE = embaralha(palavra)

print('Maximo de tentativas: 6')
for i in range(0,6):
    if i == 5:
        print(f'----- Você perdeu e não adivinhou a palavra\nela era: {palavra} -----')
        break
    print(f'Palavra embaralhada: {palavraE}')
    palavraLi = input(f'[tentativa {i+1}]Qual é a palavra: ')
    if palavraLi == palavra:
        print('----- Parabens você acertou a palavra! -----')
        break
