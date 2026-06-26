from operacoesbd import *

conexao = criarConexao('localhost', 'root', '1234', 'sistema_ouvidoria')

titulo_nova_declaracao = input('Digite um título para a declaração: ')
assunto_nova_declaracao = input('Digite o assunto da declaração: ')

categoria_nova_declaracao = int(input('Categorias \n1) Reclamação \n2) Sugestão \n3) Elogio \nDigite a categoria desejada: '))

if categoria_nova_declaracao == 1 or categoria_nova_declaracao == 2 or categoria_nova_declaracao == 3:

    if categoria_nova_declaracao == 1:
        nome_categoria = 'Reclamalção'
    elif categoria_nova_declaracao == 2:
        nome_categoria = 'Sugestão'
    else:
        nome_categoria = 'Elogio'

    consulta = 'insert into Manifestacoes (titulo,assunto,categoria) values(%s,%s,%s);'
    dados = [ titulo_nova_declaracao,assunto_nova_declaracao,nome_categoria ]

    codigo_nova_declaracao = insertNoBancoDados(conexao, consulta, dados)
    print('Manifestação cadastrada com sucesso, o código é', codigo_nova_declaracao, '!')

else:
    print('Não existe a categoria para o código informado, por favor, tente novamente.')

encerrarConexao(conexao)