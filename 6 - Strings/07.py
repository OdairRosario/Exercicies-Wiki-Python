"""
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
"""


frase = str(input('Frase: ')).upper()
qb = int(0)
vogais = [0,0,0,0,0]
for i in frase:
    print(i)
    if i == ' ':
        qb += 1
    if i == 'A': vogais[0] += 1
    if i == 'E': vogais[1] += 1
    if i == 'I': vogais[2] += 1
    if i == 'O': vogais[3] += 1
    if i == 'U': vogais[4] += 1

print(f'Frase: {frase}\nExistem {qb} espaços em branco na frase')
print('Vogais - Vezes que apareceu')
print(f'A     -  {vogais[0]}')
print(f'E     -  {vogais[1]}')
print(f'I     -  {vogais[2]}')
print(f'O     -  {vogais[3]}')
print(f'U     -  {vogais[4]}')