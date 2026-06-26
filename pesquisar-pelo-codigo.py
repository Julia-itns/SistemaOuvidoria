from operacoesbd import *

conexao = criarConexao('localhost', 'root', '1234!', 'sistema_ouvidoria')

codigo_declaracao = int(input('Digite o codigo da declaracao: '))
consulta = 'select * from Declaracoes where codigo = %s;'
dados = [ codigo_declaracao ]

declaracoes = listarBancoDados(conexao, consulta, dados)

if len(declaracoes) > 0:
    print('Declaração encontrada: Título', declaracoes[0][1], 'com categoria', declaracoes[0][3])
else:
    print('Não existe declaração para o código informado.')


encerrarConexao(conexao)