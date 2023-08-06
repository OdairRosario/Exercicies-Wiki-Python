"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
"""

nome = input('Nome:')
senha = input('Senha: ')
while(nome == senha):
    print('Senha não pode ser igual o nome.')
    nome = input('Nome: ')
    senha = input('Senha: ')