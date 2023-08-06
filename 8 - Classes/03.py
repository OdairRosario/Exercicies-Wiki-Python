"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""

class Retangulo:
    def __init__(self,LadoA, LadoB):
        self.Base = float(LadoA)
        self.Altura = float(LadoB)
    
    def MudarLados(self):
        self.Base = float(input('\nNovo valor, Medida A: '))
        self.Altura = float(input('Novo valor, Medida B: '))

    def MostraLados(self):
        print(f'LadoA: {self.Base}\nLadoB: {self.Altura}')
    
    def CalculaArea(self):
        area = (self.Base*self.Altura)
        print(f'\nA a quantidade em m² de piso: {area}')

    def CalcularPerimetro(self):
        perimetro = (self.Base + self.Altura) * 2
        print(f'\nO quantidade de rodapes em metros: {perimetro}')

if __name__ == "__main__":
    print('==== Calcula pisos e rodapés para o local ====')
    LadoA = float(input('Medida A: '))
    LadoB = float(input('Medida B: '))
    local = Retangulo(LadoA, LadoB)

    local.MostraLados()
    local.CalculaArea()
    local.CalcularPerimetro()

    local.MudarLados()
    local.MostraLados()
    local.CalculaArea()
    local.CalcularPerimetro()