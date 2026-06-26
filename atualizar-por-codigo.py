from operacoesbd import *

conexao = criarConexao('localhost', 'root', '1234', 'sistema_ouvidoria')

codigo_declaracao_atualizar = int(input('Digite o código da declaração a ser atualizada: '))
titulo_declaracao = input('Digite o título da declaração: ')
assunto_nova_declaracao: str = input('Digite o assunto da declaração: ')

consulta = 'update Declaracoes set titulo = %s, assunto = %s where codigo = %s;'
dados = [titulo_declaracao, assunto_nova_declaracao, codigo_declaracao_atualizar]

linhas_afetadas = atualizarBancoDados(conexao, consulta, dados)

if linhas_afetadas > 0:
    print('Declaração atualizada com sucesso!')
else:
    print('Não existe declaração para o código informado.')


encerrarConexao(conexao)