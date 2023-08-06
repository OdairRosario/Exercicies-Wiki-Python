"""
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, 
valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
"""
import math

ValorDivida = float(input('Valor: '))
valor = ValorDivida
juros = int()

print('/- Valor da divida / Valor dos juros / Parcelas / Valor da parcela -/')
for i in range(0,13):
    if i == 1 or i == 3 or i == 6 or i == 9 or i == 12:
        if i == 3:juros = 10
        elif i == 6:juros = 15
        elif i == 9:juros = 20
        elif i == 12:juros = 25
        else:juros = 0 
        
        valor = ValorDivida + ((ValorDivida/100) * juros)
        print(f'R${valor}            {(ValorDivida/100)*juros}                  {i}                {valor/(i):.2f}')
    else:
        continue

