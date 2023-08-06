"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.
"""
x,y,z = 1,0,0

while(z <= 500):
    z = x + y
    y = x
    x = z
    print(z)
