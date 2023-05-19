''' Não utilizei muitos comentários neste código pois ele está bem intuitivo, até mesmo
pelo nome das funções e das variáveis =) '''

def dimensoesObjeto():

    # vamos manter o user dentro de um loop para voltarmos caso respostas incorretas
    while True:
        try:
            altura = int(input('\nDigite a altura do objeto: \n'))
            comprimento = int(input('Digite o comprimento do objeto: \n'))
            largura = int(input('Digite a largura do objeto: \n'))

            # cálculo de volume 
            volume = altura * largura * comprimento

            # retorno de acordo com tabela
            if volume < 1000:
                print('O volume do objetvo é (em cm³) {:.1f}'.format(volume))
                return 10
            elif volume <= 1000 and volume < 10000:
                print('O volume do objetvo é (em cm³) {:.1f}'.format(volume))
                return 20
            elif volume <= 10000 and volume < 30000:
                print('O volume do objetvo é (em cm³) {:.1f}'.format(volume))
                return 30
            elif volume <= 30000 and volume < 100000:
                print('O volume do objetvo é (em cm³) {:.1f}'.format(volume))
                return 50
            elif volume >= 100000:
                print('Não aceitamos objetos com dimensões tão grandes\n')
                print('Digite as dimensões novamente\n')
                continue
        except:
            print('Valor incorreto!\n')
            print('Digite as dimensões novamente\n')
            continue

def pesoObjeto():

    # vamos manter o user dentro de um loop para voltarmos caso respostas incorretas
    while True:
        try:
            peso = int(input('\nDigite o peso do objeto: \n'))

            # novamente, vamos comparar o valor inputado e retornar de acordo com tabela
            if peso <= 0.1:
                return 1
            if peso <= 0.1 and peso < 1:
                return 1.25
            if peso <= 1 and peso < 10:
                return 2
            if peso <= 10 and peso < 30:
                return 3
            if peso >= 30:
                print('Não aceitamos objetos tão pesados\n')
                print('Digite o peso novamente')
                continue
        except:                 
            print('Valor incorreto\n')
            print('Digite o peso novamente\n')
            continue

def rotaObjeto():

    # vamos manter o user dentro de um loop para voltarmos caso respostas incorretas
    while True:

        try:
            print('\n***** Rotas disponiveis ***** \n')
            print('RS - De Rio de Janeiro até São Paulo')
            print('SR - De São Paulo até Rio de Janeiro')
            print('BS - De Brasília até São Paulo')
            print('SB - De São Paulo até Brasília')
            print('BR - De Brasília até Rio de Janeiro')
            print('RB - Rio de Janeiro até Brasília\n')

            rota = str(input('Digite a rota desejada: \n'))

            # vamos verificar qual a rota inputada
            if rota == 'RS' or rota == 'rs':
                return 1
            elif rota == 'SR' or rota == 'rs':
                return 1
            elif rota == 'BS' or rota == 'bs':
                return 1.2
            elif rota == 'SB' or rota == 'sb':
                return 1.2
            elif rota == 'BR' or rota == 'br':
                return 1.5
            elif rota == 'RB' or rota == 'rb':
                return 1.5
            else:
                print('Rota inválida! \n')
                print('Digite novamente a rota\n')
                continue
        except:
            print('Valor inválido! \n')
            print('Digite novamente a rota\n')
            break

#########################################################################

# aqui é nosso main 

print('Bem Vindo a Companhia de Logística de Djalma Soares de Azevedo\n S.A.')

dimensao = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()

total = dimensao * peso * rota

print('\nTotal a pagar {}, dimensão: {} * peso: {} * rota: {}'.format(total, dimensao, peso, rota))
