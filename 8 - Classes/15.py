"""
Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece 
ao bichinho e por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.
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

    def Alimentar(self, comida):
        if self.Fome >= 100:
            print('Impossivel alimentar, barriga cheia')
        else:
            self.Fome += comida*3
            if self.Fome >= 100:
                self.Fome = 100
            print(f'Alimentado com {comida} comidinhas!')
    
    def Brincar(self, tempo):#tempo em miniutos
        
        if self.Saude >= 100:
            print('Seu pet não quer brincar mais')
        else:
            self.Saude += tempo/4
            
            if self.Saude >= 100:
                self.Saude = 100
            print(f'Você brincou {tempo} minutos com seu pet')
   
    def AlterarIdade(self):
        self.Idade = int(input(f'Idade atual: {self.Idade}\nNova idade:'))
    
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
    pet.Alimentar(10)
    pet.Brincar(60)
    pet.RetornaDados()
