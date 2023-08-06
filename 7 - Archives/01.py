"""
Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
contendo um relatório dos endereços IP válidos e inválidos.
O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
"""

def verefica(ip):
    NumeroIP = ip.split('.')

    if len(NumeroIP) > 4:
        return False

    for i in NumeroIP:
        Numero = int(i)

        if Numero < 0 or Numero > 255:
            return False
    
    return True
validos, invalidos = [], []

with open('1Ips.txt', 'r') as arquivo:
    for linha in arquivo:
        if verefica(linha) == True:
            validos.append(linha)
        else:
            invalidos.append(linha)

with open('1IpsRelatorio.txt', 'w') as a:
    a.write('[Enderecos validos:]\n')
    a.writelines(validos)
    a.write('[Enderecos invalidos:]\n')
    a.writelines(invalidos)

print('Ips vereficado com sucesso. Verefique o relatorio')