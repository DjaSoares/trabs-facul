# boas vindas do programa
print('Bem Vindo a Loja do Djalma Soares de Azevedo')

# vamos pegar o valor do produto
valor = float(input('Entre com o valor do produto (ex: 10.00): '))

# declaração de variaveis
desconto = 0.00
quantidade = 0

# loop para mantermos o programa girando
while True:
    # verificação se o valor de fato é válido
    if valor <= 0.00:
        valor = float(input('Valor inválido, entre com um novo valor: '))
        continue
    # caso positivo, vamos solicitar a quantidade e também verificar validade da mesma
    else:
        if quantidade <= 0:
            quantidade = int(input('Entre com quantidade do produto: '))
            continue

        # a partir daqui sabemos que o valor é válido e quantidade também, vamos comparar com os descontos disponíveis
        elif quantidade <= 9:
            print('Valor total sem desconto: R$ {:.2f}'.format(valor))
            print('Valor total com desconto: R$ {:.2f}'.format(valor))
            break
        elif quantidade >= 10 and quantidade <= 99:
            desconto = valor * 0.05          # cálculo de desconto básico
            print('Valor total sem desconto: R$ {:.2f}'.format(valor))
            print('Valor total com desconto: R$ {:.2f}'.format(valor - desconto))     # cálculo de total com desconto
            break
        elif quantidade >= 100 and quantidade <= 999:
            desconto = valor * 0.10
            print('Valor total sem desconto: R$ {:.2f}'.format(valor))
            print('Valor total com desconto: R$ {:.2f}'.format(valor - desconto))
            break
        elif quantidade >= 1000:
            desconto = valor * 0.15
            print('Valor total sem desconto: R$ {:.2f}'.format(valor))
            print('Valor total com desconto: R$ {:.2f}'.format(valor - desconto))
            break
