"""
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. 
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo,
um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, 
um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam
salários nos seguintes intervalos de valores:
$200 - $299 [0]
$300 - $399 [1]
$400 - $499 [2]
$500 - $599 [3]
$600 - $699 [4]
$700 - $799 [5]
$800 - $899 [6]
$900 - $999 [7]
$1000 em diante [8]

Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
"""
vetorContadores = [0,0,0,0,0,0,0,0,0]
Valor = float()

x = int()
for i in range(0,10):
    valor = float(input('valor de vendas: '))
    valor = ((valor/100) * 9) + 200
    if valor > 1000:
        x = 10
    else:
        x = int(str(valor)[0])
    vetorContadores[x-2] += 1

for i in range(200,1000, 100):
    if i >= 1000:
        print(f'$1000 em diante -> {vetorContadores[8]}')
    else:
        x = int(str(int((i/100)-2))[0])
        print(f'R${i} - R${i+99} -> {vetorContadores[x]}')

   