from operacoesbd import *

def pesquisar_declaracao_pela_categoria(conexao):
    categoria_pesquisa = int(
        input('Categorias \n1) Reclamação \n2) Sugestão \n3) Elogio \nDigite a categoria desejada:'))
    if categoria_pesquisa == 1 or categoria_pesquisa == 2 or categoria_pesquisa == 3:

        if categoria_pesquisa == 1:
            nome_categoria = 'Reclamação'
        elif categoria_pesquisa == 2:
            nome_categoria = 'Sugestão'
        else:
            nome_categoria = 'Elogio'

        consulta = 'select * from Declaracoes where categoria = %s;'
        dados = [nome_categoria]
        declaracoes = listarBancoDados(conexao, consulta, dados)

        if len(declaracoes) > 0:
            print("Lista de Filmes")
            for item in declaracoes:
                print("- Código", item[0], "\nNome:", item[1], "\nCom categoria:", item[2])

        else:
            print("Não existem declarações a serem exibidas.")


def atualizar_declaracao(conexao):
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


def obter_quantidade_declaracoes(conexao):
    consulta = 'select count(*) from Declaracoes;'
    quantidade_declaracoes = listarBancoDados(conexao, consulta)

    print('Atualmente existe(m)', quantidade_declaracoes[0][0], 'declaraçãos(ões)')


def remover_declaracao_pelo_codigo(conexao):
    codigo_declaracao_remover = int(input('Digite o código da declaração a ser removida: '))

    consulta = 'delete from Declaracoes where codigo = %s;'
    dados = [codigo_declaracao_remover]

    linhas_afetadas = excluirBancoDados(conexao, consulta, dados)

    if linhas_afetadas > 0:
        print('Declaracão removida com sucesso!')
    else:
        print('Não existe declaração para o código informado')

def inserir_declaracao(conexao):
    titulo_nova_declaracao = input('Digite o título da declaração: ')
    assunto_nova_declaracao = input('Digite o assunto da declaração: ')


    categoria_nova_declaracao = int(input('Categorias \n1) Reclamação \n2) Sugestão \n3) Elogio \nDigite a categoria desejada: '))

    if categoria_nova_declaracao == 1 or categoria_nova_declaracao == 2 or categoria_nova_declaracao == 3:

        if categoria_nova_declaracao == 1:
            nome_categoria = 'Reclamação'
        elif categoria_nova_declaracao == 2:
            nome_categoria = 'Sugestão'
        else:
            nome_categoria = 'Elogio'

        consulta = 'insert into Declaracoes (titulo,assunto,categoria) values(%s,%s,%s);'
        dados = [titulo_nova_declaracao, assunto_nova_declaracao, nome_categoria]

        codigo_nova_declaracao = insertNoBancoDados(conexao, consulta, dados)
        print('Declaração cadastrada com sucesso, o código é', codigo_nova_declaracao, '!')

    else:
        print('Não existe a categoria para o código informado, por favor, tente novamente.')


def pesquisar_declaracao_pelo_codigo(conexao):
    codigo_declaracao = int(input('Digite o codigo da declaração: '))
    consulta = 'select * from Declaracoes where codigo = %s;'
    dados = [codigo_declaracao]

    declaracoes = listarBancoDados(conexao, consulta, dados)

    if len(declaracoes) > 0:
        print('Declaração encontrada:\nNome:', declaracoes[0][1], '\nAssunto:', declaracoes[0][2], '\nCom categoria:', declaracoes[0][3])
    else:
        print('Não existe declaração para o código informado.')


def listar_declaracoes(conexao):
    consulta = 'select * from Declaracoes;'

    declaracoes = listarBancoDados(conexao, consulta)

    if len(declaracoes) > 0:
        print("Lista de Declarações")
        for item in declaracoes:
            print("- Código", item[0], "\nTítulo:", item[1], "\nAssunto:", item[2], "\nCom categoria:", item[3])

    else:
        print("Não existem declarações a serem exibidas.")