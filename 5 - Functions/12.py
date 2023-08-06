"""
Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra
string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar
npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que
todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
"""

from random import *

def embaralhar(palavra):
    retorno = str('')
    palavra = list(palavra)
    for i in range(0,len(palavra)):
        retorno += choice(palavra)
        palavra.remove(retorno[i])
    return retorno
    
print(embaralhar(input('an word: ')))