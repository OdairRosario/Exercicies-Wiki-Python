"""
Controle de cotas de disco. A ACME Inc., uma organização com mais de 1500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço em disco ocupado pelas contas dos usuários, e identificar 
os usuários com maior espaço ocupado. Através de um aplicativo baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado usuarios.txt:

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o primeiro campo corresponde ao login do usuário e o segundo ao espaço em disco ocupado pelo seu diretório home.
A partir deste arquivo, você deve criar um programa que gere um relatório, chamado relatório.txt, no seguinte formato:

ACME Inc.           Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB            16,85%
2    anderson       1187,99 MB            46,02%
3    antonio         117,73 MB             4,56%
4    carlos           87,03 MB             3,37%
5    cesar             0,94 MB             0,04%
6    rosemary        752,88 MB            29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. 
A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. 
O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
Recursos adicionais: opcionalmente, desenvolva as seguintes funcionalidades:

[ x ] Ordenar os usuários pelo percentual de espaço ocupado;
[ x ] Mostrar apenas os n primeiros em uso, definido pelo usuário;

[ x ] Gerar a saída numa página html;
[ x ] Criar o programa que lê as pastas e gera o arquivo inicial;
"""
import os
from functions import * # algumas funções para o programa funcionar


class App():
    def __init__(self):
        self.Dados = dict()

    def CarregaArquivo(self,arquivo):
        with open(arquivo, 'r') as a:
            for linha in a:
               self.Dados[linha[0:15]] = ByteConvert(float(linha[15:]))

    def CarregaPasta(self, PATH):
        NomesPastas = [item.name for item in os.scandir(PATH) if not item.name.startswith('.') and item.is_dir()]
        CaminhoPastas = [item.path for item in os.scandir(PATH) if not item.name.startswith('.') and item.is_dir()]
        for i in range(0, len(NomesPastas)):
            self.Dados[NomesPastas[i]] = ByteConvert(Size(CaminhoPastas[i]))


    def RetornaRelatorioTerminal(self):
        dados_values = Ordena(list(self.Dados.values()))
        dados_keys = list(self.Dados.keys())
        quantidade_MemoriaTotal = ([item for item in  dados_values])
        quantidade_MemoriaTotal = sum(quantidade_MemoriaTotal)

        print('ACME Inc.           Uso do espaço em disco pelos usuários\n'+'--'*31)
        print('Nr.  Usuário        Espaço utilizado        % do uso')
        for i in range(0,len(dados_keys)):
            Porcentagem = Percentage(dados_values[i],quantidade_MemoriaTotal)
            texto = '{}    {}  {:.2f} MB{:.2f}%'.format(i+1, dados_keys[i],dados_values[i], Porcentagem)
            print('{}    {}  {:.2f} MB{}{:.2f}%'.format(i+1, dados_keys[i],dados_values[i], Blank(texto),Porcentagem))
        print('\nEspaço total ocupado: {:.2f} MB\nEspaço medio ocupado: {:.2f} MB'.format(quantidade_MemoriaTotal, quantidade_MemoriaTotal/len(dados_keys) ))
    
    def RetornaRelatorioArquivo(self):
        dados_values = Ordena(list(self.Dados.values()))
        dados_keys = list(self.Dados.keys())
        quantidade_MemoriaTotal = ([item for item in  dados_values])
        quantidade_MemoriaTotal = sum(quantidade_MemoriaTotal)
        try:
            os.mkdir('Relatorios')
        except FileExistsError: 
            pass
        with open('.\Relatorios\Relatorio.txt', 'w') as arquivo:
            arquivo.write('ACME Inc.           Uso do espaco em disco pelos usuarios\n'+'--'*31)
            arquivo.write('\nNr.  Usuario        Espaco utilizado        % do uso\n')
            for i in range(0,len(dados_keys)):
                Porcentagem = Percentage(dados_values[i],quantidade_MemoriaTotal)
                texto = '{}    {}  {:.2f} MB{:.2f}%'.format(i+1, dados_keys[i],dados_values[i], Porcentagem)
                arquivo.write('{}    {}  {:.2f} MB{}{:.2f}%\n'.format(i+1, dados_keys[i],dados_values[i], Blank(texto),Porcentagem))
            arquivo.write('\nEspaco total ocupado: {:.2f} MB\nEspaco medio ocupado: {:.2f} MB'.format(quantidade_MemoriaTotal, quantidade_MemoriaTotal/len(dados_keys) ))
    
        print('Arquivo Gerado com sucesso!')   

    def RetornaRelatorioHtml(self):
        dados_values = Ordena(list(self.Dados.values()))
        dados_keys = list(self.Dados.keys())
        quantidade_MemoriaTotal = ([item for item in  dados_values])
        quantidade_MemoriaTotal = sum(quantidade_MemoriaTotal)

        try:
            os.mkdir('Relatorios')
        except  FileExistsError:
            pass
    
        pagina = open('.\Relatorios\Relatorio.html', 'w')
        
        CODIGO_HTML = """<p align="center">
    <b> 
        Inc.           Uso do espaco em disco pelos usuarios<br>
        ------------------------------------------------------------------------
    </b>
    <table border=1>
        <tr>
            <th>Nr.</th>
            <th>Usuario</th>
            <th>Espaco utilizado</th>
            <th>% do uso</th>
        </tr>
    """

        pagina.write(CODIGO_HTML)

        #parte 2
        for i in range(len(dados_values)):
            Porcentagem = Percentage(dados_values[i],quantidade_MemoriaTotal)
            CODIGO_HTML = """
        <tr>
        <td>{}</td>
        <td>{}</td>
        <td>{:.2f} MB</td>
        <td>{:.2f}%</td>
    </tr>""".format(i+1, dados_keys[i],dados_values[i],Porcentagem)
            pagina.write(CODIGO_HTML)

        # parte 3
        CODIGO_HTML = """
    </table>
    <b>
        Espaco total ocupado: {:.2f} MB<br>
        Espaco medio ocupado: {:.2f} MB<br>
    </b>
</p>""".format(quantidade_MemoriaTotal, quantidade_MemoriaTotal/len(dados_keys) )
        pagina.write(CODIGO_HTML)

        pagina.close()
        print('tabela html gerada com sucesso')


def main():
    app = App()
    opcao = str(input('1 - Ler relatorio do problema\n2 - Carregar arquivos de uma pasta\n'))
    if opcao == '1':
        arquivo = ".\Dados\Dados.txt"
        app.CarregaArquivo(arquivo)
        while(True):
            opcao = int(input('1 - No terminal\n2 - Em um arquivo txt\n3 - Numa tabela HTML\nReceber relatorio por onde: '))
            if opcao == 1:
                app.RetornaRelatorioTerminal()
                break
            elif opcao == 2:
                app.RetornaRelatorioArquivo()
                break
            elif opcao == 3:
                app.RetornaRelatorioHtml()
                break
            else:
                print('Digite uma opção existente.')

    elif opcao == '2':
        pasta = input('Cole aqui o caminho da pasta(ex: D:\Python\Estrutura sequencial) ')
        app.CarregaPasta(pasta)
        while(True):
            opcao = int(input('1 - No terminal\n2 - Em um arquivo txt\n3 - Numa tabela HTML\nReceber relatorio por onde: '))
            if opcao == 1:
                app.RetornaRelatorioTerminal()
                break
            elif opcao == 2:
                app.RetornaRelatorioArquivo()
                break
            elif opcao == 3:
                app.RetornaRelatorioHtml()
                break
            else:
                print('Digite uma opção existente.')
        
if __name__ == "__main__":
    main()
