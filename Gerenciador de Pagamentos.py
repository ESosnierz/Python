#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- Á vista (dinheiro ou cheque) : 10% de desconto
#- Á vista no cartão : 5% de desconto
#- Em até 2x no cartão: preço normal
#- 3x ou mais no cartão: 20% de juros
print('\033[7;41m===================== Lojas Sosnierz =====================\033[m')
print(''' ''')
valor = float(input('\033[1;36mQual o valor do praduto ? R$ '))
print('''\033[1;31;40m Escolha uma das formas de pagamento!\033[m
\033[1;33m[ 1 ] - Á vista (dinheiro ou cheque) : 10% de desconto
[ 2 ] - Á vista no cartão : 5% de desconto
[ 3 ] - Em até 2x no cartão: preço normal
[ 4 ] - 3 até 15 vezes no cartão: 20% de juros\033[m''')
opcao = int(input('\033[1;36mQual opcão de pagamento? : '))
if opcao == 1:
    total = valor - (valor * 10 /100)
    desconto = valor - total
    print('\033[1;31mValor do produto é de R$ {:.2f}'.format(valor))
    print('\033[1;31mValor com 10% de desconto é de R$ {:.2f}'. format(desconto))
    print('\033[1;31mValor total a pagar é de R$ {:.2f}'.format(total))
elif opcao == 2:
    total = valor - (valor * 5 / 100)
    desconto = valor - total
    print('\033[1;31mValor do produto é de R$ {:.2f}'.format(valor))
    print('\033[1;31mValor com 5% desconto é de R$ {:.2f}'.format(desconto))
    print('\033[1;31mValor total a pagar é de R$ {:.2f}'.format(total))
elif opcao == 3:
    div = valor / 2
    print('\033[1;31mValor do produto é de R$ {:.2f}'.format(valor))
    print('\033[1;31mValor em 2x de R$ {:.2f}'.format(div))
elif opcao == 4:
    total = valor + (valor * 20 /100)
    qpacerlas = int(input('\033[1;36mQuantidade de parcelas : '))
    parcelas = total / qpacerlas
    juros = total - valor
    if qpacerlas <= 15:
        print('\033[1;31mValor do produto é de R$ {:.2f}'.format(valor))
        print('\033[1;31mValor acrescentado de juros é de R$ {:.2f}'.format(juros))
        print('\033[1;31mValor total do produto com juros é de {:.2f} em {}x é de R$ {:.2f}\033[m'.format(total, qpacerlas, parcelas))
    else:
        print('\033[1;30;41mNão é permitido parcelar mais que 15X\033[m')
else:
    print('\033[1;31mVocê não digitou nenhuma das Opções.')