"""
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos:
[0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

"""
zeroTw, TwFf, FfSv, SvHd = int(0), int(0), int(0), int(0)

while True:
    n = int(input('valor[negativo encerra]: '))

    if n < 0:
        break
    elif n >= 0 and n <= 25:
        zeroTw += 1
    elif n > 25 and n <= 50:
        TwFf += 1
    elif n > 50 and n <= 75:
        FfSv += 1
    elif n > 75 and n <= 100:
        SvHd += 1
    else:
        continue

print(f'[ 0- 25] -> {zeroTw}\n[26- 50] -> {TwFf}\n[51- 75] -> {FfSv}\n[76-100] -> {SvHd}')
