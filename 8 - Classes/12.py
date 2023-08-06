"""
Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria,
com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros.
Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma poupança com um
saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.
"""

class contaBancaria():
    def __init__(self,inicial):
        self.saldoInicial = float(inicial)
        

class contaInvestimento(contaBancaria):
    def __init__(self, inicial, juros):
        super().__init__(inicial)
        self.taxaJuros = float(juros)

    def adicioneJuros(self):
        self.saldoInicial = ((self.saldoInicial * self.taxaJuros)/ 100) + self.saldoInicial
        print(f'Com {self.taxaJuros}% de juros aplicado: ',self.saldoInicial)
    
if __name__ == "__main__":
    conta = contaInvestimento(1000,10)
    conta.adicioneJuros()
    conta.adicioneJuros()
    conta.adicioneJuros()
    conta.adicioneJuros()
    conta.adicioneJuros()