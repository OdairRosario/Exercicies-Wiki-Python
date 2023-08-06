"""
Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""

VetorA, VetorB, VetorC= list(), list(), list()

for i in range(0,10):
    VetorA.append(float(input('Valor VetorA: ')))
    VetorB.append(float(input('Valor VetorB: ')))
for i in range(0,10):
    VetorC.append(VetorA[i])
    VetorC.append(VetorB[i])

print(f'{VetorA}\n{VetorB}\n{VetorC}')