import os

def Blank(texto):
    return " " * 15
def ByteConvert(Bytes, tipo = 'M'):
    """
    Para converter byte em Kbyte,MegaByte,GigaByte
    """
    if tipo == 'K': return Bytes/ 1024
    if tipo == 'M': return Bytes/ (1024)**2
    if tipo == 'G': return Bytes/ 1**9
    
    
def Percentage(valor, total):
    """
    REGRA DE TRÊS:

        valores      porcentagens
       valor_atual       100%

           total          x
    """ 

    return (valor * 100) / total

def Ordena(valores):
    # o python possui o metodo sorted() que ordena, mas mesmo assim para praticar: este é o algoritimo BubbleSort
    aux = int()
    for i in range(len(valores)):
        for j in range(i+1, len(valores)):
            if valores[i] > valores[j]:
                valores[i], valores[j] = valores[j], valores[i]
    return valores

def Size(caminhoPasta):
    """
    Função para calcular a quantidade de memoria que uma pasta ocupa
    """
    if os.path.isdir(caminhoPasta):
        tamanho = 0
        for arquivo in os.listdir(caminhoPasta):
            tamanho += Size(os.path.join(caminhoPasta, arquivo))
        return tamanho
    else:
        #neste caso não é uma pasta então retorna-se o tamanho do arquivo
        return os.path.getsize(caminhoPasta)

texto = "https://www.youtube.com/watch?v=nt7mnMn6DBs&list=PLDRcEdRquEb0iYBa3Q4PF_UtgDbJvfqq6&index=48"
