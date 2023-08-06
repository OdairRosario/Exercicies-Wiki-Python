"""
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""
VetorA, VetorB, VetorC, VetorD = list(), list(), list(), list()

for i in range(0, 10):
    VetorA.append(float(input('[Vetor A]Valor: ')))
    VetorB.append(float(input('[Vetor B]Valor: ')))
    VetorC.append(float(input('[Vetor C]Valor: ')))
    VetorD.append(VetorA[i])
    VetorD.append(VetorB[i])
    VetorD.append(VetorC[i])

print(f'{VetorA}\n{VetorB}\n{VetorC}\n{VetorD}')