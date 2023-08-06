"""
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, 
com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa 
dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles,
para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento.
O programa deverá receber um número indeterminado de entradas, cada uma contendo: 
um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado 
Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""
quantidadeDosDefeitos = [0,0,0,0]
TipoDeDefeitos = ['necessita da esfera', 'necessita de limpeza', 'necessita troca do cabo ou conector', 'quebrado ou inutilizado']
codigo, contador = int(), int()
while True:
    codigo = -1
    while codigo < 0 or codigo > 4: 
        codigo = int(input(f'[DIGITE CORRETAMENTE OS DADOS] index: {contador+1}\n(0-Sair/1-necessita da esfera/2-necessita de limpeza/3-necessita troca do cabo ou conector/4-quebrado ou inutilizado)\nCodigo: '))
    if codigo == 0:
        break
    quantidadeDosDefeitos[codigo-1] += 1
    contador+=1
print(f'Quantidade de mauses: {sum(quantidadeDosDefeitos)}\nSituação                                         Quantidade           Percentual')
for i in range(0,4):
    while len(TipoDeDefeitos[i]) < len(TipoDeDefeitos[2]): TipoDeDefeitos[i] += ' '
    porcentagem = (quantidadeDosDefeitos[i] *100) / sum(quantidadeDosDefeitos)
    print(f'{i+1}- {TipoDeDefeitos[i]}                {quantidadeDosDefeitos[i]}                 {porcentagem:.2f}%')
    """
    Def por
    50  100
    15   x
    50x = 15*100
    x = 1500/50
    x = 30

    """