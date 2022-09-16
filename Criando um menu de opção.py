'''Cire um programa que leia dois valores e mostre um menu na tela:
[] somar
[] multiplicar
[] maior
[] novos números
[] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''
#------------------------ inicio do programa --------------------
from time import sleep
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
#---------------------- Inicio da função-------------------
opcao = 0
while opcao != 5:
    print(''' Escolhas uma opção para realizar a operação desejada:
[ 1 ] - Somar
[ 2 ] - Multiplicar
[ 3 ] - Maior valor
[ 4 ] - Escolher novos números
[ 5 ] - Sair do programa
''')
    opcao = int(input('Informe a opção desejada: '))
    if opcao == 1:
        soma =  n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        multi = n1 * n2
        print('A multiplicação de {} X {} é {}'.format(n1, n2, multi))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('Entre os valores {} e {} o maior é {}'.format(n1, n2, maior))
        else:
            maior = n2
            print('Entre os valores {} e {} o maior é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os valores novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente! ')
    print('*'*20)
    sleep(2)
print('Programa finalizado!')