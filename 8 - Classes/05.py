"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero
e os demais atributos são obrigatórios.
"""

class ContaCorrente:
    def __init__(self,numero,nome, saldo=0):
        self.NumeroConta = numero
        self.NomeCorrentista = nome
        self.saldo = saldo
    
    def alterarNome(self):
        self.NomeCorrentista = input(f'Nome atual: {self.NomeCorrentista}\nAlterar para:')

    def Deposito(self):
        valor = float(input('Valor a depositar: '))
        self.saldo += valor
        print(f'Valor atualizado!\nvalor atual: {self.saldo}')

    def Saque(self):
        valor = float(input('Valor do saque: '))
        self.saldo -= valor
        print(f'Valor atualizado!\nvalor atual: {self.saldo}')

if __name__ == "__main__":
    numero = input('Numero da conta: ')
    Nome = input('Nome do correntista: ')
    saldo = float()
    if int(input('1 -> digitar saldo\n2 -> não atribuir')) == 1:
        saldo = float(input('Saldo[opcional - enter para não atribuir]: '))
    else: saldo = 0
    conta = ContaCorrente(numero,Nome,saldo)
    conta.alterarNome()
    conta.Deposito()
    conta.Saque()
