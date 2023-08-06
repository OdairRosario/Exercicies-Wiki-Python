"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo,
a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos 
clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada
quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados
os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da médiadas alturas e dos pesos dos clientes
"""

mb_codigo, mb_altura, mb_peso = int(), int(), float() # mais baixo
ma_codigo, ma_altura, ma_peso = int(), int(), float() # mais alto
mm_codigo, mm_altura, mm_peso = int(), int(), float() # mais magro
mg_codigo, mg_altura, mg_peso = int(), int(), float() # mais gordo
contador = int(0)

while True:
    codigo = int(input('Codigo[0 - encerra]: '))
    if codigo == 0: break

    altura = int(input('Altura[Cm]: '))
    while altura <= 0: 
        altura = int(input('VALOR INVALIDO, DEVE SER MAIOR QUE 0\n[Altura[Cm]'))
    peso = float(input('Peso[Kg]: '))
    while peso <= 0: 
        peso = float(input('VALOR INVALIDO DEVE SER MAIOR QUE 0\nPeso[Kg]: '))

    if contador == 0:
        mg_altura = mm_altura = mb_altura = ma_altura = altura
        mg_peso = mm_peso = mb_peso = ma_peso = peso
        mg_codigo = mm_codigo = mb_codigo = ma_codigo = codigo
    else:
        if altura < mb_altura:
            mb_altura = altura
            mb_peso = peso
            mb_codigo = codigo
        if altura > ma_altura:
            ma_altura = altura
            ma_peso = peso
            ma_codigo = codigo
        if peso < mm_peso:
            mm_altura = altura
            mm_peso = peso
            mm_codigo = codigo
        if peso > mg_peso:
            mg_altura = altura
            mg_peso = peso
            mg_codigo = codigo

    contador += 1

print(f'Mais baixo: codigo ->{mb_codigo} peso ->{mb_peso} altura ->{mb_altura}')
print(f'Mais alto : codigo ->{ma_codigo} peso ->{ma_peso} altura ->{ma_altura}')
print(f'Mais magro: codigo ->{mm_codigo} peso ->{mm_peso} altura ->{mm_altura}')
print(f'Mais gordo: codigo ->{mg_codigo} peso ->{mg_peso} altura ->{mg_altura}')