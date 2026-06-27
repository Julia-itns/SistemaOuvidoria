#Felipe Lavrado
#Julia Inês
# Luiz Miguel
# Maria Claudia

from operacoesbd import *

conexao = criarConexao('localhost', 'root', '1234', 'sistema_ouvidoria')

consulta = 'select count(*) from Declaracoes;'
quantidade_declaracoes = listarBancoDados(conexao, consulta)

print('Atualmente existe(m)', quantidade_declaracoes[0][0], 'declaração(ões)')

encerrarConexao(conexao)