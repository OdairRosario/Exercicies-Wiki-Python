"""
Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. 
Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira.
Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos 
(alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). 
Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.

"""

import random

class Pet:

    def __init__(self,Nome, Idade):
        self.Nome = str(Nome)
        self.Fome = int(random.randint(30,70))
        self.Saude = int(random.randint(30,70))
        self.Idade = int(Idade)

        self.MaxFome = int(100)
        self.MaxSaude = int(100)

    def AlterarNome(self):
        self.Nome = input(f'Nome atual: {self.Nome}\nNovo nome: ')

    def Alimentar(self, comida):
        if self.Fome < 100:
            self.Fome += comida*3
            if self.Fome >= 100:
                self.Fome = 100
    
    def Brincar(self, tempo):#tempo em miniutos
        if self.Saude < 100:
            self.Saude += tempo/4
            if self.Saude >= 100:
                self.Saude = 100
            
   
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
        """
            Retorna os dados(dados reais) de todos os pets 
        """
        print(f"\nNome: {self.Nome}\nFome: {self.Fome}\nSaude: {self.Saude}\nIdade: {self.Idade}\nMaximo de Fome: {self.MaxFome}\nMaximo de saude: {self.MaxSaude}")

def main():
    quantidade = int(input('quantos bichos na fazenda: '))
    vetor = fazenda(quantidade)
    while(True):
        print(f'Quantidade de bichos na fazenda: {len(vetor)}')
        print('--'*10)
        menu = input('\n1 - Alimentar\n2 - Brincar\n3 - Ver status\n4- Alterar nome\n5 - Alterar idade\n6 - Sair\n'+ '--'*10+'\nEscolha[Lembre-se que esta ação é tomada para todos o bichinhos]:')
        if menu == '1':
            comida = int(input('Dar quantas comidinhas para os pets?: '))
            for i in range(0,len(vetor)):
                vetor[i].Alimentar(comida)
            print(f'Alimentados com {comida} comidinhas!')

        elif menu == '2':
            tempo = int(input('Brincar por quantos minutos com os pets?: '))
            for i in range(0, len(vetor)):
                vetor[i].Brincar(tempo)
            print(f'Você brincou {tempo} minutos com seus pets')
        
        elif menu == '3':
            for i in range(0,len(vetor)):
                print(f'{i+1} - {vetor[i].Nome}')
            indice = int(input('Ver dados de qual:')) - 1
            vetor[indice].RetornaDados()

        elif menu == '4':
            for i in range(0,len(vetor)):
                print(f'{i+1} - {vetor[i].Nome}')
            indice = int(input('Alterar nome de qual?: ')) - 1
            vetor[indice].AlterarNome()

        elif menu == '5':
            for i in range(0,len(vetor)):
                print(f'{i+1} - {vetor[i].Nome}')
            indice = int(input('alterar a idade de qual?: ')) - 1
            vetor[indice].AlterarIdade()

        elif menu == '6':
            print('fechando..')
            break;

        elif menu == "secret":
            for i in range(0,len(vetor)):
                vetor[i].str()
        
        else:
            print('Algo de errado! Tente novamente')

def fazenda(quantidade = 5):
    vetor = list()
    for i in range(0,quantidade):
        vetor.append(Pet(f'Bichinho {i+1}', random.randint(1,20)))
    return vetor

if __name__ == "__main__":
    main()
