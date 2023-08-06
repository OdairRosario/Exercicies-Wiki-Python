"""
Valida e corrige número de telefone. Faça um programa que leia um número de telefone, 
e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. 
O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133

"""
def CharRemove(string, letter = ' '):
    """
        input: 
            STRING - text for remove the letter   
            LETTER - an char for remove, if no receive the char blank space will be removed
        output: the text without the letter
    """
    retorno = str()
    for i in range(0,len(string)):
        if string[i] != ' ':
            retorno += string[i]

def CharAppend(string,char, position = -1):  
    """
        input: 
            STRING -  to add a new char 
            CHAR - one char for add in the string
            POSITON - the position for add the new char, but if not recieve will be add in the last position
        output: 
            STRING - string with the new char added in the position
    """
    retorno = str('')
    for i in string:
        if i == string[position]: 
            retorno +=  char
        retorno += i

    return retorno

def verefica(numero):
    x= str('3')
    if '-' in numero: CharRemove(numero, '-')
    if len(numero) == 7:
        numero = x + numero
        print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
        print(f'telefone corrigido sem formatação: {numero}')
        print(f'telefone corrigido com formatação: {numero[0:4]}-{numero[4:]}')
    print('Telefone validado;')

print('Valida e corrige número de telefone')
numero = str(input('Telefone: '))
verefica(numero)
    