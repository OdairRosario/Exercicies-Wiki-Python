"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

n = int(input('N-ésimo: '))
x, y, z = int(1),int(0),int(0)

while(True):
    if x == n:
        break

    z = (x) + (y)# 1
    y = x#1
    x = z#1
    
    print(z, end=' ')
