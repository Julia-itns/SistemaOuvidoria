#Felipe Lavrado
#Julia Inês
# Luiz Miguel
# Maria Claudia

from operacoesbd import *

conexao = criarConexao('localhost', 'root', '1234', 'sistema_ouvidoria')

codigo_declaracao_remover = int(input('Digite o código da declaração a ser removida: '))

consulta = 'delete from Declaracoes where codigo = %s;'
dados = [codigo_declaracao_remover]

linhas_afetadas = excluirBancoDados(conexao, consulta, dados)

if linhas_afetadas > 0:
    print('Declaração removida com sucesso!')
else:
    print('Não existe declaração para o código informado')

encerrarConexao(conexao)