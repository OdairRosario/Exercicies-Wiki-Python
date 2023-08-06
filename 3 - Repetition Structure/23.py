"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""

numDivisoes, num =  0,0
while(num <= 0): num = int(input('mostrar primos de 1 a N: '))

for numero in range(1, num + 1):
    primo = True
    for i in range(2, int(numero / 2 + 1)):
        numDivisoes += 1
        if (numero % i == 0):
            primo = False
            break
    if (primo == True):
        print(numero, end = ' ')

print ('\nnum de divisoes:', numDivisoes)