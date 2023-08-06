"""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""

class Bola():
    def __init__(self,cor,circun,material):
        self.cor = str(cor)
        self.circun = float(circun)
        self.material = str(material)
    
    def trocaCor(self):
        self.cor = input('Nova cor: ')
        
    def mostraCor(self):
        print('A cor da bola é:',self.cor)


if __name__ == "__main__":
    cor = input('Cor: ')
    circun = float(input('Circunferencia: '))
    material = input('Material: ')

    bola = Bola(cor,circun, material)

    bola.mostraCor()
    bola.trocaCor()
    bola.mostraCor()