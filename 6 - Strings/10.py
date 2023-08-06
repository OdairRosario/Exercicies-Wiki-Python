"""
Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
"""

def NumeroExtenso(numero):
    if numero > 99 or numero < 0:
        return 'Numero invalido: Num deve ser menor que 100 e maior que  0'
    dezenas = {
        2: 'Vinte e ',
        3: 'Trinta e ',
        4: 'Quarenta e ',
        5: 'Cinquenta e ',
        6: 'Sessenta e ',
        7: 'Setenta e ',
        8: 'Oitenta e ',
        9: 'Noventa e '
    }

    unidades = {
        0: 'zero',
        1: 'um',
        2: 'dois',
        3: 'três',
        4: 'quatro',
        5: 'cinco',
        6: 'seis',
        7: 'sete',
        8: 'oito',
        9: 'nove',
        10: 'dez',
        11: 'onze',
        12: 'doze',
        13: 'treze',
        14: 'quatorze',
        15: 'quinze',
        16: 'dezesseis',
        17: 'dezessete',
        18: 'dezoito',
        19: 'dezenove'
    }
    if numero < 20:
        return unidades[numero]
    else:
        x = str(numero)[0]
        y = str(numero)[1]
        return (dezenas[int(x)] + unidades[int(y)])


num = int(input('Digite um valor: '))

print('Numero por extenso: ',NumeroExtenso(num))
