""" 
Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.
"""

def ValidaCpf(cpf):
    valido = bool(True)
    if len(cpf) != 14:
        return False

    try:
        if int(cpf[0:3]) > 1000 and int(cpf[0:2]) >= 0:
            valido = False
            print('a')
        if int(cpf[4:7]) > 1000 and int(cpf[0:2]) >= 0:
            print('b')
            valido = False
        if int(cpf[8:11]) > 1000 and int(cpf[0:2]) >= 0:
            print('c')
            valido = False
        if int(cpf[12:]) > 99 and int(cpf[12]) >= 0:
            print('d')
            valido = False
        if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
            valido = False
    except:
        return False
   
    return valido


CPF = str()
while ValidaCpf(CPF) == False:
    print(f'cpf invalido!')
    CPF =  str(input('Digite seu cpf[xxx-xxx-xxx-xx]: ' ))

print(f'cpf aceito!')