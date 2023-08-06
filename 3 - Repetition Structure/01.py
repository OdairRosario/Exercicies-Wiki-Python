"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue 
pedindo até que o usuário informe um valor válido.
"""
nota = float(input('Nota: '))
while True:
    if nota <= 10 and nota >= 0:
        break
    else:
        print('Preencha corretamente!')
        nota = float(input('Nota:'))