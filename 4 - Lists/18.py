"""Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. 
Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. 
Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação python. Para computar cada voto, a telefonista 
digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi 
encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. 
Após o final da votação, o programa deverá exibir:
O total de votos computados;
Os númeos e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. 
O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. 
Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o 
valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo.
Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao 
resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
"""


jogadores = list()
x,y = int(), int()

for i in range(1,24):
    jogadores.append(0)

while  True:
    numero = int(input('Numero da camisa do jogador[0-Fim]: '))
    if numero == 0:
        break
    while numero > 23 or numero < 0: numero = int(input('Informe um valor entre 1 e 23 ou 0 para sair!\n Numero da camisa do jogador[0-Fim]: '))
    jogadores[numero-1] += 1
    
    

print(f'Foram computados {sum(jogadores)} votos')
for i in range(0,23):
    if jogadores[i] == max(jogadores): y = i
    if jogadores[i] == 0:
        continue
    else:
        x = float((100*jogadores[i]/ sum(jogadores)))
        """
        POR   VOTOS
        100   100
        x     25
        100x = 100*25
        x = 2500 / 100
        x = 25
        """
        print(f'Jogador {i+1} com {jogadores[i]} votos ({x:.1f}%)')

x = float((100*jogadores[y]/ sum(jogadores)))
print(f'O melhor jogador foi o número {y+1}, com {jogadores[y]} votos, correspondendo a {x:.1f}% do total de votos.')