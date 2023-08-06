"""
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. 
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos 
valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar 
o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""

vetor = [0,0,0,0,0,0]
sistemas = ['Windows Server', 'Unix', 'Linux', 'Netwere', 'Max OS', 'Outro']
voto, x  = int(), int()
while True:
    voto = int(-1)
    voto = int(input('1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outros\n[0- Encerra]: '))
    while voto < 0 or voto > 6: voto = int(input('Não adcionado! Digite um valor valido!\n11- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outros\n[0- Encerra]: '))
    if voto == 0 :
        break
    vetor[voto-1] += 1

if sum(vetor) == 0:
    pass
else:
    print('Sistema Operacional     Votos   %\n-------------------     -----   ---')
    for i in range(0,len(sistemas)):
        x = float(100*vetor[i]) / sum(vetor)
        """
        POR  VOTO
        100  100
        X     25
        100X = 100*25
        [...]
        """
        while len(sistemas[i]) < len(sistemas[0]): sistemas[i] += ' '
        print(f'{sistemas[i]}            {vetor[i]}     {x:.0f}%')
    print(f'-------------------     -----\nTotal                     {sum(vetor)}')

print('Programa finalizado!')