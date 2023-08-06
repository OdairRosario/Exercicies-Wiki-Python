"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""

valores = list()
soma, media, AcimaMedia, AbaixoDeSete = float(0), float(0), int(0), int(0)
while True:
    valor = float(input('Nota[-1 Encerra]: '))
    valores.append(valor)
    if valor == -1:
        valores.pop(-1)
        break

print(f'Foram lidos {len(valores)} valores\nOrdem inversa:')

for i in range(len(valores)-1, -1, -1):
    print(valores[i], end=' ')
    soma += valores[i]

for i in range(len(valores)-1, -1, -1):
    print(valores[i])

media = soma/len(valores)

for i in valores:
    if i > media:
        AcimaMedia += 1
    if i < 7:
        AbaixoDeSete += 1 

print(f'Soma dos valores: {soma}\nmedia dos valores {media:.2f}\nquantidade de valores acima da media: {AcimaMedia}\nquantidade de valores abaixo de sete: {AbaixoDeSete}')
print('Programa finalizado!')