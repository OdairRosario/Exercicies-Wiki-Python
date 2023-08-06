"""
Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras,
como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete
uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes
e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa
que peça uma texto e transforme-o para a grafia leet speak.
"""

def LeetSpekGenerator(palavra):
    retorno = str()
    letras ={
        'A': '4',
        'B': '6',
        'C': '(',
        'D': '[)',
        'E': '3',
        'F': ']]=',
        'G': '&',
        'H': '#',
        'I': '!',
        'J': ',|',
        'K': ']{',
        'L': '1',
        'M': '(V)',
        'N': '(/)',
        'O': '()',
        'P': '[]D',
        'Q': '(,)',
        'R': '1²',
        'S': '$',
        'T': '7',
        'U': '(_)',
        'V': '\/',
        'W': '´//',
        'X': '%',
        'Y': '´/',
        'Z': '"/_',
        ' ': ' '
    }
    for i in palavra.upper():
        retorno += letras[i]
    return retorno
    

print('gerador de leet spek')
a = input('texto:')
print(a)
print('Em leet spek: ',LeetSpekGenerator(a))