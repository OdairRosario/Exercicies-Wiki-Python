"""
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.
"""

n = int(input('N: '))
m = int(1)
s, soma = float(), float()
for i in range(1,n+1):
    s = i/m
    m += 2
    soma += s
    
print(f'Soma: {soma:.2f}')