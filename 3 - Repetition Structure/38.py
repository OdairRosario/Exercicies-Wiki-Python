"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo 
que o usuário digite o salário inicial do funcionário.
"""

salario_I = float(input ('Salario inicial: '))
salario_F = float(salario_I)
taxa = float(1.5)
ano = int(1997)

for i in range(1997,2021):
    salario_F += (salario_F/ 100) * taxa
    taxa += 1.5

print(f'Salario inicial: R${salario_I}0 no ano {ano}\nsalario final: R${int(salario_F)}.00 no ano {i}')