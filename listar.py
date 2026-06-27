#Felipe Lavrado
#Julia Inês
# Luiz Miguel
# Maria Claudia

from operacoesbd import *

conexao = criarConexao('localhost', 'root', '1234', 'sistema_ouvidoria')
consulta = 'select * from Declaracoes;'

declaracoes = listarBancoDados(conexao, consulta)

if len(declaracoes) > 0:
    print("Lista de Declarações")
    for item in declaracoes:
        print("- Código", item[0], "\nTítulo:", item[1], "\nAssunto:", item[2], "\nCom categoria:", item[3])

else:
    print("Não existem declarações a serem exibidas.")

encerrarConexao(conexao)