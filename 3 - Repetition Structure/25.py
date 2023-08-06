"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a 
média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é 
jovem, adulta ou idosa, conforme a média calculada.
"""

n, media = int(0), 0 

while n <= 0: n = int(input('Quantas Pessoas?[+ que 1]: ')) 

for i in range(1,n + 1):
    idade = int(input('idade: '))
    media += idade
