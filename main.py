from operacoesbd import *

conexao = criarConexao('localhost', 'root', '1234', 'sistema_ouvidoria')


encerrarConexao(conexao)