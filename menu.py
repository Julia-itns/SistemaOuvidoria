from ouvidoria import *

conexao = criarConexao('localhost', 'root', '1234', 'sistema_ouvidoria')



while True:
    print('\n1) Inserir \n2) Listar \n3) Pesquisar pelo código \n4) Excluir pelo código \n5) Quantidade de Declarações \n6) Atualizar Declaração pelo Código \n7) Listar Declarações por Categoria \n8) Sair')
    opcao = int(input('Digite a sua opção: '))

    if opcao == 1:
        inserir_declaracao(conexao)


    elif opcao == 2:
        listar_declaracoes(conexao)

    elif opcao == 3:
        pesquisar_declaracao_pelo_codigo(conexao)

    elif opcao == 4:
        remover_declaracao_pelo_codigo(conexao)

    elif opcao == 5:
        obter_quantidade_declaracoes(conexao)

    elif opcao == 6:
        atualizar_declaracao(conexao)

    elif opcao == 7:
        pesquisar_declaracao_pela_categoria(conexao)

    elif opcao == 8:
        break

encerrarConexao(conexao)
print('Obrigado!')