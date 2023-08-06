"""
Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita
da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos.
Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS
é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma
seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
"""


def CharRemove(string, char = ' '):
    retorno = str()
    for i in range(0,len(string)):
        if string[i] != ' ':
            retorno += string[i]
    return retorno
def StrInvert(string):
    retorno = str()
    for i in range(len(string)-1, -1, -1): 
        retorno += string[i]
    return retorno

string = CharRemove(str(input('texto: ')))
StringInvertida = CharRemove(string)
StringInvertida = StrInvert(StringInvertida)
        
if StringInvertida.upper() == string.upper():
    print(f'Sim é um palíndromo\n{string} - {StringInvertida}')
else:
     print(f'Não é um palíndromo\n{string} - {StringInvertida}')
