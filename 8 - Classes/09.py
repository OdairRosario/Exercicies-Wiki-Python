"""
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
O valor do centro do objeto deve ser mostrado na tela
Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
"""

class Ponto:
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
    
    def MostraValores(self):
        return f"x: {self.x}\ny: {self.y}"

class Retangulo(Ponto):
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura
    
    def EncontraCentro(self):
        centro = Ponto(self.largura / 2, self.altura / 2)
        return f'O centro do retangulo se encontra em:\n{centro.MostraValores()}'

if __name__ == "__main__":
    opc = 'S'
    while(True):
        if opc[0].upper() == 'N':
            break
        else:
            largura = float(input('Largura do retangulo: '))
            altura = float(input('Altura do retangulo: '))
            retan = Retangulo(altura,largura)
            print(retan.EncontraCentro())
            opc = input('Achar outro centro?(S-Sim / N-Não)')