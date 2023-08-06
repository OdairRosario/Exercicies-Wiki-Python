"""
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""

class bombaCombustível:
    def __init__(self,tipo,valor,quantidade):
        self.tipoCombustivel = str(tipo)
        self.valorLitro = float(valor)
        self.quantidadeCombustivel = float(quantidade)

    def abastecerPorValor(self):
        if self.quantidadeCombustivel < 0:
            print('Combustivel indisponivel')
        else:
            print(f'Quantidade disponivel de combustivel: {self.quantidadeCombustivel}')
            quanty = float(input('Quanto deseja abastecer:\nR$')) 
            self.quantidadeCombustivel -= quanty
            quanty /= self.valorLitro
            print('{:.2f} litros de {} adcionado ao tanque'.format(quanty, self.tipoCombustivel))

    def abastecerPorLitro(self):
        if self.quantidadeCombustivel < 0:
            print('Combustivel indisponivel')
        else:
            print(f'Quantidade disponivel de combustivel: {self.quantidadeCombustivel}')
            preco = float(input('Quantos litros deseja abastecer?: ')) 
            self.quantidadeCombustivel -= preco
            preco *= self.valorLitro
            print('R${:.2f} devem ser pagos'.format(preco))

    def alterarValor(self):
        self.valorLitro = float(input(f'Tipo do combustivel: {self.tipoCombustivel}\nPreço atual: R${self.valorLitro}\nNovo valor: R$'))
        print('valor alterado com sucesso!')

    def  alterarCombustivel(self):
        self.tipoCombustivel = str(input(f'Tipo atual: {self.tipoCombustivel}\nNovo tipo: '))
        print('Valor alterado com secesso!')
    
    def alterarQuantidadeCombustivel(self):
        self.quantidadeCombustivel += float(input(f'Quantidade atual: {self.quantidadeCombustivel}\n adcionar quanto?: '))
        print(f'Quantidade adcionada com sucesso\nNova quantidade: {self.quantidadeCombustivel}')

if __name__ == "__main__":
    a = bombaCombustível('Gasolina', 4.50, 355)
    a.abastecerPorLitro()
    a.abastecerPorValor()
    a.alterarValor()
    a.alterarCombustivel()
    a.alterarQuantidadeCombustivel()
    a.abastecerPorLitro()
    a.abastecerPorValor()