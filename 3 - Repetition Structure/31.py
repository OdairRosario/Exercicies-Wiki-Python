"""
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido
de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final 
da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para 
então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar 
a próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...
"""
total = float()
contador = int(0)

while True:
    while True:
        contador += 1
        valor = float(input('Preço[0 finaliza]: '))
        print(f'Produto 1: R$ {valor}')
        total += valor

        if valor == 0:
            print('Total :', total)
            dinheiro = float(input('Dinheiro: '))
            if dinheiro < total:
                while dinheiro < total: float(input('Insira um valor maior que o da compra'))
            
            dinheiro = dinheiro - total
            print('Troco: R$ ', dinheiro)
            print('--' * 4)
            break
