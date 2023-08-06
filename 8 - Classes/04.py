"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""

class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = str(nome)
        self.idade = int(idade)
        self.peso = float(peso)
        self.altura = float(altura)

    def Envelhercer(self):
        print('Envelheceu um ano')
        if self.idade < 21:
            self.altura += 0.005
            print('E aumentou altura em 0.5! ')
        self.idade += 1

    def Engordar(self):
        print('Engordou 5Kg')
        self.peso += 5 

    def emagrecer(self):
        print('emagreceu 5Kg')
        self.peso -= 5
    
    def crescer(self):
        print('Cresceu 3cm!')
        self.altura += 0.03

    def MostraDados(self):
        print(f'\nnome: {self.nome}\nidade: {self.idade}\npeso: {self.peso}\naltura: {self.altura:.2f}')


if __name__ == "__main__":
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    peso = float(input('Peso: '))
    altura = float(input('altura[ex: 1.75]: '))
    pessoa = Pessoa(nome, idade, peso, altura)

    pessoa.MostraDados()
    pessoa.Envelhercer()
    pessoa.Engordar()
    pessoa.Engordar()
    pessoa.crescer()
    pessoa.emagrecer()
    
    pessoa.MostraDados()

