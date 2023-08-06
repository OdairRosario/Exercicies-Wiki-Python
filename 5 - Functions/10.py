"""
Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, 
obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. 
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, 
você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar 
este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
"""
 
from random import *

def geraDados():
    return randint(2,12)

def VereficaDados(dado):
    if dado == 7 or dado == 11:
        print(f'dados: {dado}\nVocê é um natural, Ganhou!')
        return False
    elif dado == 2 or dado == 3 or dado == 12:
        print(f'dados: {dado}\nCraps! Você perdeu') 
        return False
    else:
        print(f'dados: {dado}\nPonto!')
        global x
        x = dado
        return True

def VereficaPonto(continuar):
    global contador,dado, x
    while continuar == True:
        contador+=1
        print('--'*10)
        input(f'Jogada {contador}\n Prescione qualquer letra para jogar...')
        dado = geraDados()
        print(f'dados: {dado}')
        if dado == x:
            print('GANHOU!')
            continuar = False
        if dado == 7:
            print('PERDEU!')
            continuar = False
        else:
            if dado != x: 
                print('PODES CONTINUAR JOGANDO')
                continuar = True

def main():
    input(f'Jogada {contador}\n Prescione qualquer letra para jogar...')
    dado = geraDados()
    continuar = VereficaDados(dado)
    VereficaPonto(continuar)
    print('Programa finalizado')

contador, x = int(1), int(0)

main()

