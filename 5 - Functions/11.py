"""
Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e 
devolva uma string no formato D de mesPorExtenso de AAAA. 
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
"""

def DataPorExtenso(data):
    Dias = {
        1:'UM', 2:'DOIS', 3:'TRÊS', 4:'QUATRO', 5:'CINCO', 6:'SEIS', 7:'SETE', 8:'OITO', 9:'NOVE', 10:'DEZ', 11:'ONZE', 
        12:'DOZE', 13:'TREZE', 14:'QUATORZE', 15:'QUINZE', 16:'DEZESSEIS', 17:'DEZESSETE', 18:'DEZOITO', 19:'DEZENOVE', 
        20:'VINTE', 21:'VINTE E UM', 22:'VINTE E DOIS', 23:'VINTE E TRÊS', 24:'VINTE E QUATRO', 25:'VINTE E CINCO', 
        26:'VINTE DE SEIS', 27:'VINTE E SETE', 28:'VINTE E OITO', 29:'VINTE E NOVE', 30:'TRINTA', 31:'TRINTA E UM',
        2000: 'DOIS MIL E'
    }
    meses = {
        1: 'JANEIRO',
        2: 'FEVEREIRO',
        3: 'MARÇO',
        4: 'ABRIL',
        5: 'MAIO',
        6: 'JUNHO',
        7: 'JULHO',
        8: 'AGOSTO',
        9: 'SETEMBRO',
        10:'OUTUBRO',
        11:'NOVEMBRO',
        12:'DEZEMBRO'
    }
    texto = str()

    i = int(data[0:2])
    texto += f'{Dias[i]} DE '
    i = int(data[4:5])
    texto += f'{meses[i]} DE {Dias[2000]} {Dias[int(data[9:])]}'
    return texto

def Valida(data):
    if len(data) != 10:
        return False
    elif data[2] != '/' or data[5] != '/':
        return False
    elif int(data[0:2]) > 31 or int(data[3:5]) > 12:
        return False
    elif int(data[0:2]) < 0 or int(data[3:5]) < 0:
        return False
    else:
        return True

#10/20/3003  01-2-34-5-6789

data = input('Digite sua data de nascimento no formato DD/MM/AAAA\nData:')

while Valida(data) == False:
    data = input('Dados invalidos\nDigite sua data de nascimento no formato DD/MM/AAAA\nData:')


print(DataPorExtenso(data))