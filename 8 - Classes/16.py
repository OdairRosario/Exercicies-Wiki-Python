"""
Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do objeto.
Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário.
Dica: acrescente um método especial str() à classe Bichinho.
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
    
    def str(self):
        print(f"Nome: {self.Nome}\nFome: {self.Fome}\nSaude: {self.Saude}\nIdade: {self.Idade}\nMaximo de Fome: {self.MaxFome}\nMaximo de saude: {self.MaxSaude}")

if __name__ == "__main__":
    nome = input('Nome de seu pet: ')
    idade = int(input('Idade dele: '))
    pet = Pet(nome,idade)
    while(True):
        menu = input('--'*10+ '\n1 - Alimentar\n2 - Brincar\n3 - Ver status\n4- Alterar nome\n5 - Alterar idade\n6 - Sair\n'+ '--'*10+'\nEscolha:')
        if menu == '1':
            pet.Alimentar(int(input('Dar quantas comidinhas para o pet?: ')))
        elif menu == '2':
            pet.Brincar(int(input('Brincar por quantos minutos com o pet?: ')))
        elif menu == '3':
            pet.RetornaDados()
        elif menu == '4':
            pet.AlterarNome()
        elif menu == '5':
            pet.AlterarIdade()
        elif menu == '6':
            print('fechando..')
            break;
        elif menu == "secret":
            pet.str()
        else:
            print('Algo de errado! Tente novamente')
