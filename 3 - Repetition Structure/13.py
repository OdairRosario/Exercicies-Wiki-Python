"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""

x = int(input('Base: '))
y = int(input('Expoente: '))
resultado = int(x)

for i in range(0,y-1):
    resultado = resultado*x
    
print(f'{x} elevado a {y} -> {resultado}')



