"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""

class Quadrado:
    def __init__(self, lado):
        self.TamanhoLado = float(lado)
    
    def MudarValorLado(self):
        self.TamanhoLado = float(input('Nova medida do lado: '))

    def MostraValorLado(self):
        print('O valor do lado é: ', self.TamanhoLado)

    def CalcularArea(self):
        print('\nA area deste quadrado é: ',self.TamanhoLado*self.TamanhoLado)

if __name__ == "__main__":
    lado = float(input('Lado do quadrado: '))
    quadrado = Quadrado(lado)
    quadrado.MostraValorLado()
    quadrado.CalcularArea()
    quadrado.MudarValorLado()
    quadrado.MostraValorLado()
    quadrado.CalcularArea()