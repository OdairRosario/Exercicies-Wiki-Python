"""
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F
"""

x, nome = str(), str(input('Nome: ')).upper()

for i in range(len(nome), 0, -1):
    print(nome[:i])