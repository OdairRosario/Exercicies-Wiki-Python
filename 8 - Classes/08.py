"""
Classe Macaco: 
Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) 
pelo menos os métodos comer(), verBucho() e digerir(). 
Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes
e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

Sim é possivel :Joy:
"""


class Macaco:
    def __init__(self,nome):
        self.nome = str(nome)
        self.estomago = str()
    
    def Comer(self, comida):
        self.estomago = comida

    def verBucho(self):
        print(f'No bucho tem: {self.estomago}')
   
    def digerir(self):
        self.estomago = ""
        print('Digerido')

if __name__ == "__main__":
    macaco1 = Macaco('cabeção')
    macaco2 = Macaco('Bocão')

    macaco1.Comer('Porco')
    macaco1.verBucho()
    macaco1.digerir()

    macaco2.Comer('Melão')
    macaco2.verBucho()
    macaco2.digerir()

    macaco1.Comer('Macaco')
    macaco1.verBucho()
    macaco1.digerir()

