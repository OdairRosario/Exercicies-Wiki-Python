"""
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0.
Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
Forneça um método adicionarGasolina( ), para abastecer o tanque. 
Exemplo de uso:
meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
meuFusca.andar(100);            # anda 100 quilômetros.
meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.
"""

class carro():
    def __init__(self,consumo):
        self.consumoPorKm = float(consumo)
        self.nivelCombustivel = float(0)
    
    def andar(self,distancia):
        self.nivelCombustivel -= ((distancia/1000) * self.consumoPorKm)
    
    def obterGasolina(self):
        print('Nivel atual de gasolina: {:.2f} litros'.format(self.nivelCombustivel))
    
    def adicionarGasolina(self,quanty):
        self.nivelCombustivel += quanty

if __name__ == "__main__":
    meuFusca = carro(15)
    meuFusca.adicionarGasolina(20)
    meuFusca.andar(100)# metros
    meuFusca.obterGasolina()