
# ---------------- variáveis globais --------------

pecas = []
codigo_index = 0

# -------------------------------------------------

def removerPeca():

    codigo = int(input('Por gentileza, qual o código do produto que deseja remover?\n'))

    for i in pecas: # vamos varrer a lista
        if i['codigo'] == codigo: # se o código bater, ai sim removemos
            pecas.remove(i)
            print('Produto removido com sucesso!\n')


def cadastrarPeca(codigo):

    pecasTemp = {}

    print('Código da peça: {}'.format(codigo_index))

    nome = input('Por gentileza digite o nome da peça: \n')
    fabricante = input('Por gentileza digite o fabricante da peça: \n')
    valor = float(input('Por gentileza digite o valor a peça: \n'))

    # vamos passar os valores inputados para nosso dicionário temporário
    pecasTemp = {'codigo' : codigo, 'nome' : nome, 'fabricante' : fabricante, 'valor' : valor }

    # agora copiamos para nossa lista de dicionários
    pecas.append(pecasTemp.copy())


def consultarPeca():

    print('****** MENU ******')
    print('1 - Consultar todas as peças')
    print('2 - Consultar peças por código')
    print('3 - Consultar peças por fabricante')
    print('4 - Retornar')

    opcao = int(input('Digite a opção desejada: \n'))

    # vamos fazer o menu exibido acima funcionar
    if opcao == 1:
        for i in pecas: # vamos varrer a lista
            for key, value in i.items():  # vamos pegar os itens dentro do dicionario e printar
                print('Campo: {}, Valor: {}\n'.format(key, value))

    elif opcao == 2:
        codigo = int(input('Digite o código da peça: \n'))

        for i in pecas: # vamos varrer a lista
            if i['codigo'] == codigo: # vamos localizar o valor digitado
                for key, value in i.items(): # localizamos? ok, vamos mostrar a peça
                    print('Campo: {}, Valor: {}\n'.format(key, value))

    elif opcao == 3:
        fabricante = str(input('Digite o fabricante da peça: \n'))

        for i in pecas:  # vamos varrer a lista
            if i['fabricante'] == fabricante:  # vamos localizar o valor digitado
                for key, value in i.items():  # localizamos? ok, vamos mostrar a peça
                    print('Campo: {}, Valor: {}\n'.format(key, value))

    elif opcao == 4:
        return

# ----------------- main --------------

while True:

    print('******** Bem vindo ao controle de estoque da bicicletaria de Djalma Soares ********')
    print('Escolha a opção desejada: \n')

    print('1 - Cadastrar peça')
    print('2 - Consultar peças')
    print('3 - Remover peças')
    print('4 - Sair\n')

    # aqui inputamos qual opção o user deseja
    opcao_menu = int(input())

    # menus em ação!
    if opcao_menu == 1:
        codigo_index += 1
        cadastrarPeca(codigo_index)
    elif opcao_menu == 2:
        consultarPeca()
    elif opcao_menu == 3:
        removerPeca()
    elif opcao_menu == 4:
        break


    for i in pecas: # vamos varrer a lista
            if i['codigo'] == codigo: # vamos localizar o valor digitado
                for key, value in i.items(): # localizamos? ok, vamos mostrar a peça
                    print('Campo: {}, Valor: {}\n'.format(key, value))

    elif opcao == 3:
        fabricante = str(input('Digite o fabricante da peça: \n'))

        for i in pecas:  # vamos varrer a lista
            if i['fabricante'] == fabricante:  # vamos localizar o valor digitado
                for key, value in i.items():  # localizamos? ok, vamos mostrar a peça
                    print('Campo: {}, Valor: {}\n'.format(key, value))

    elif opcao == 4:
        return

# ----------------- main --------------

while True:

    print('******** Bem vindo ao controle de estoque da bicicletaria de Djalma Soares ********')
    print('Escolha a opção desejada: \n')

    print('1 - Cadastrar peça')
    print('2 - Consultar peças')
    print('3 - Remover peças')
    print('4 - Sair\n')

    # aqui inputamos qual opção o user deseja
    opcao_menu = int(input())

    # menus em ação!
    if opcao_menu == 1:
        codigo_index += 1
        cadastrarPeca(codigo_index)
    elif opcao_menu == 2:
        consultarPeca()
    elif opcao_menu == 3:
        removerPeca()
    elif opcao_menu == 4:
        break
