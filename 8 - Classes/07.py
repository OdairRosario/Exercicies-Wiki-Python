"""
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade 

Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs:
Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre
os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por
que ela pode ser calculada a qualquer momento.
"""

class Pet:

    def __init__(self,Nome, Idade):
        self.Nome = str(Nome)
        self.Fome = int(50)
        self.Saude = int(50)
        self.Idade = int(Idade)

        self.MaxFome = int(100)
        self.MaxSaude = int(100)

    def AlterarNome(self):
        self.Nome = input(f'Nome atual: {self.Nome}\nNovo nome: ')

    def AlterarFome(self):
        fome = int(input(f'Fome atual: {self.Fome}\naumentar ou diminuir para[Max: 100 e Min: 0]: '))
        if fome < 0 or fome > 100:
            print('Valor invalido')
        else: self.Fome = fome
    
    def AlterarSaude(self):
        saude = int(input(f'Saude atual:{self.Saude}\naumentar ou diminuir para[Max: 100 e Min: 0]: '))
        if saude < 0 or saude > 100:
            print('Valor invalido')
        else: self.Saude = saude
    def AlterarIdade(self):
        self.Idade = int(input(f'Idade atual: {self.Idade}\nNova Idade: '))
    
    def RetornaDados(self):
        humor = (self.Saude + self.Fome) / 2
        if humor >= 75:
            humor = str('Muito Feliz')
        elif humor >= 50 and humor < 75:
            humor = str('Feliz')
        elif humor < 50 and humor >= 25:
            humor = str('sereno') 
        elif humor < 25 and humor >= 10:
            humor = str('mau')
        elif humor < 10:
            humor = str('muito mau')
        
        print(f"""            nome: {self.Nome}
           Idade: {self.Idade}
            Fome: {self.Fome}
           Saude: {self.Saude}
           Humor: {humor}
        """)
    
if __name__ == "__main__":
    nome = input('Nome de seu pet: ')
    idade = int(input('Idade dele: '))
    pet = Pet(nome,idade)
    pet.RetornaDados()
