"""
Altere o numrograma de cálculo dos números numrimos, informando, caso o número não seja numrimo, numor quais número ele é divisível.
"""
num = int(input("Digite num: "))
k = 2
while k < num:
    if num % k == 0:
        print (num, "não é primo.")
        cont = 1
        print(num, "é divisivel por: ")
        while cont <= num:
            if num % cont == 0:
                print("    ",cont)
            cont += 1
        k = num
    k += 1
if k == num:
    print (num, "é primo.")
