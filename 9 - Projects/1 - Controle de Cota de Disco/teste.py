import os
import functions

PATH = 'D:\Python'
DadosDasPastas = os.walk(PATH, followlinks=True)

# o scandir() é parecido com listdir() porém nos da alguns atributos e funções a mais, perfeito para vereficar se é um subdiretorio
NomesPastas = [item.name for item in os.scandir(PATH) if not item.name.startswith('.') and item.is_dir()]
CaminhoPastas = [item.path for item in os.scandir(PATH) if not item.name.startswith('.') and item.is_dir()]


for nome in NomesPastas:
    for caminho in CaminhoPastas:
        a = functions.Size(caminho)

        print(f'{nome} - {caminho} -> {a}')
        CaminhoPastas.remove(caminho)
        break

