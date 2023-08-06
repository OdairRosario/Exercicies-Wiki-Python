"""
O cardápio de uma lanchonete é o seguinte:

Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""

total, codigo, quantidade = int(), int(), int()
print("Especificação   Código  Preço\nCachorro Quente 100     R$ 1,20\nBauru Simples   101     R$ 1,30\nBauru com ovo   102     R$ 1,50")
print("Hambúrguer      103     R$ 1,20\nCheeseburguer   104     R$ 1,30\nRefrigerante    105     R$ 1,00")
while True:
    codigo = int(input('Codigo[0-encerra]: '))
    if codigo == 0:
        break
    while codigo <100 or codigo > 105: codigo = int(input('Entrada invalida! \nCodigo[0-encerra]'))
    quantidade = int(input('Quantos?: '))
    if codigo == 100 or codigo == 103: preco = 1.20
    if codigo == 101 or codigo == 104: preco = 1.30
    if codigo == 102: preco = 1.50
    if codigo == 103: preco = 1.20
    if codigo == 105: preco = 1

    total += preco*quantidade
    print(f'Valor a ser pago: {preco*quantidade:.2f}')
print(f'Preço total: {total}')