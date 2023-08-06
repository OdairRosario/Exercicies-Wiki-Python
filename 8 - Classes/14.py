"""
Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente
o salário do funcionário em uma certa porcentagem.
Exemplo de uso:
  harry=funcionário("Harry",25000)
  harry.aumentarSalario(10)

"""

class Funcionario():
    def __init__(self,nome, salario):
        self.nome = str(nome)
        self.salario = float(salario)

    def ObterDados(self):
        print(f'Nome: {self.nome}\nSalario: {self.salario}')

    def aumentarSalario(self,porcentagem):
        self.salario += ((self.salario * porcentagem) / 100)

if __name__ == "__main__":
    eu = Funcionario('Odair', 1816.99)
    eu.ObterDados()
    eu.aumentarSalario(10)
    eu.ObterDados()
    