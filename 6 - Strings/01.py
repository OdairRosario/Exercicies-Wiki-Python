"""
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
"""

string1 = str(input('String 1: '))
string2 = str(input('String 2: '))

print(f'Tamanho de "{string1}": {len(string1)}')
print(f'Tamnho de "{string2}": {len(string2)}')

if len(string1) != len(string2):
    print('As duas strings são de tamanhos diferentes.')
else: 
    print('As duas strings são de tamanhos iguais.')

if string1 != string2:
    print('As duas strings possuem conteúdo diferente.')
else: 
    print('As duas strings possuem conteúdo igual.')