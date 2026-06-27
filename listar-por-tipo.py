#Felipe Lavrado
#Julia Inês
# Luiz Miguel
# Maria Claudia

from operacoesbd import *

conexao = criarConexao('localhost', 'root', '1234', 'sistema_ouvidoria')

categoria_pesquisa = int(input('Categorias \n1) Reclamação \n2) Sugestão \n3) Elogio \nDigite a categoria desejada:'))
if categoria_pesquisa == 1 or categoria_pesquisa == 2 or categoria_pesquisa == 3:

    if categoria_pesquisa == 1:
        nome_categoria = 'Reclamação'
    elif categoria_pesquisa == 2:
        nome_categoria = 'Sugestão'
    else:
        nome_categoria = 'Elogio'

    consulta = 'select * from Declaracoes where categoria = %s;'
    dados = [ nome_categoria ]
    declaracoes = listarBancoDados(conexao, consulta, dados)

    if len(declaracoes) > 0:
        print("Lista de declarações")
        for item in declaracoes:
            print("- Código", item[0] , 'com categoria', item[4])

    else:
        print("Não existem declarações a serem exibidas.")

encerrarConexao(conexao)