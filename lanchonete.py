# códigos de menu disponíveis
codigos = [100, 101, 102, 103, 104, 105, 200, 201]

# boas vindas do programa & menu
print('Bem Vindo a lanchonete do Djalma Soares de Azevedo')
print('         ********Cardápio********')
print('''       Código Descrição          Valor(R$)
        100        Cachorro-Quente            9,00
        101        Cachorro-Quente Duplo  11,00
        102        X-Egg                  12,00
        103        X-Salada               13,00
        104        X-Bacon                    14,00
        105        X-Tudo                 17,00
        200        Refrigerante Lata      5,00
        201        Chá Gelado             4,00
            \n''')

# variáveis para dados
valorTemp = 0.00
prosseguir = 0

# vamos manter o loop sempre rodando já que é um menu
while True:
    codigo = int(input('Entre com o código desejado: \n'))

    # verificamos se o código está dentro dos disponíveis
    if codigo in codigos:

        # caso positivo, de acordo com o código alimentamos o valor total
        if codigo == 100:
            valorTemp += 9.00
        elif codigo == 101:
            valorTemp += 11.00
        elif codigo == 102:
            valorTemp += 12.00
        elif codigo == 103:
            valorTemp += 13.00
        elif codigo == 104:
            valorTemp += 14.00
        elif codigo == 105:
            valorTemp += 17.00
        elif codigo == 200:
            valorTemp += 5.00
        elif codigo == 201:
            valorTemp += 4.00

        prosseguir = int(input('''Deseja pedir mais algo?
                                      1 - Sim
                                      0 - Nao   \n'''))

        if prosseguir == 1:
            continue
        else:
            # valor total já alimentado, vamos apenas printas
            print('Valor total a ser pago: {}\n'.format(valorTemp))
            break


    else:
        # caso código seja inválido, voltamos ao menu principal
        print('Código inválido, digite novamente\n')
        continue
