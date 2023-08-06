"""
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

maior,menor = 0,0
ler = int(input('Quantos valores?: '))

for i in range(0,ler):
    x = float(input('Valor[0-1000]: '))

    while(x >1000 or x < 0):
        x =float(input('Valor entre 0 e 1000:'))

    if i == 0:
        maior = menor = x
    elif maior < x:
        maior = x
    elif menor > x:
        menor = x
    
print(f'{ler} valores lidos\nmaior: {maior}\nmenor: {menor}')