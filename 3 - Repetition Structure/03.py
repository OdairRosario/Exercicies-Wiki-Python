"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

nome = input('Nome: ')
idade = int(input('Idade: '))
salario = float(input('Salario: '))
sexo = str(input('Sexo[M/F]: '))
Ec = str(input('Estado civil[S-Solteiro/C-Casado/V-Viuvo/D-Divorciado]: ')).upper()
Ec = Ec[0]
certo = int(0)

while(True):
    if len(nome) <= 3: nome = input('Min. 3 caracteres\nNome: ')
    else: certo += 1

    if idade <= 0 and idade >= 150: 
        idade = int(input('Idade entre 0-150\nIdade: '))
    else: certo += 1

    if salario <= 0:
        salario = float(input('Salario tem que ser maior que zero\nSalario:'))
    else: certo += 1

    if sexo[0].upper() != 'M' and sexo[0].upper() != 'F':
        sexo = str(input('Digite o dado corretamente\nSexo[M-Masculino/F-Feminino]: ')).upper()
    else: certo += 1

    if Ec != 'S' and Ec != 'C' and Ec != 'V' and Ec != 'D':
        Ec = str(input('Estado civil[S/C/V/D]: ')).upper()
        Ec = Ec[0]
    else: certo += 1


    if certo  == 5:
        break
