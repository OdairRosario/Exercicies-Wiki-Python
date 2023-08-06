"""
Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). 
Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.
"""

class Funcionario():
    def __init__(self,nome, salario):
        self.nome = str(nome)
        self.salario = float(salario)

    def ObterDados(self):
        print(f'Nome: {self.nome}\nSalario: {self.salario}')

if __name__ == "__main__":
    eu = Funcionario('Odair', 1816.99)
    eu.ObterDados()
    