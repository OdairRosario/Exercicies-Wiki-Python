"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
"""

class Tv:
    def __init__(self):
        self.MaxCanal = 100
        self.MaxVolume = 16
        self.MinVolume = 0

        self.volume = 16
        self.canal = 10

    def MudarCanal(self):
        canal = int(input('Numero canal[100 canais disponiveis]: '))
        if canal > self.MaxCanal:
            print('canal invalido')
        
        else:
            self.canal = canal

    def Aumentar(self):
        if self.volume < self.MaxVolume:
            self.volume += 1
        
        else: 
            pass
        print(f'Volume: {self.volume}/{self.MaxVolume}')
    
    def Diminuir(self):
        if self.volume <= self.MinVolume:
            pass
        
        else:
            self.volume -= 1
        print(f'Volume: {self.volume}/{self.MaxVolume}')

if __name__ == "__main__":
    tela = Tv()
    tela.MudarCanal()
    tela.Aumentar()
    tela.Diminuir()