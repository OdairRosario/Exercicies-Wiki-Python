"""
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO
"""

x, nome = str(), str(input('Nome:')).upper()

for i in nome:
    x+= i
    print(x)
