#Make a program for a paint store. The program should ask for the size in square meters of the area to be painted.
#Consider that the coverage of the paint is 1 liter for every 3 square meters and that the paint is sold in 18 liter cans, which cost R$ 80.00.
#Inform the user the spoonfuls of paint cans to be purchased and the total price.
import math

tamanho = float(input("quantos m² a area a ser pintada tem?: "))
Litro = int(3) # quantidade coberta por litro
lata18L = float(80) # preco de uma lata



latasN = math.ceil(tamanho / (Litro*18))

preco = latasN * lata18L

print("quantidade de latas: ",latasN )
print("preço: ",preco)
