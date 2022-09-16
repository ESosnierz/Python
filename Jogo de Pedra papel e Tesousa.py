#Crie um prgrama que faça o computador jogar (JOKENPÔ) com você.
print('\033[1;41m===================== Vamos Jogar ? =====================\033[m')
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''\033[1;31;40m Suas Opções:\033[m
\033[1;33m[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA\033[m''')
jogador = int(input('\033[1;31m O que você escolhe ? '))
print('-=' * 15)
print('Jo...')
sleep(1) # tempod e 1 segundo
print('Ken..')
sleep(1)
print('Poooo!')
print(' ')
print('Eu escolhi {}'.format(itens[computador]))
print('Você escolheu {}'.format(itens[jogador]))
print('-=' * 15)
if computador == 0: # CPU ESCOLHE PEDRA
    if jogador == 0:
        print('\033[1;33m Empate, vamos novamente ? ')
    elif jogador == 1:
        print('\033[1;32m Parabéns, você Ganhou !')
    elif jogador == 2:
        print('\033[1;31m haha, eu ganhei !')
    else:
        print('\033[1;33;40m Jogada INVÁLIDA! ')
elif computador == 1: # CPU ESCOLHE PAPEL
    if jogador == 0:
        print('\033[1;31m haha, eu ganhei ! ')
    elif jogador == 1:
        print('\033[1;33m Empate, vamos novamente ? !')
    elif jogador == 2:
        print('\033[1;32m Parabéns, você Ganhou ! !')
    else:
        print('\033[1;33;40m Jogada INVÁLIDA! ')
elif computador == 2: # CPU ESCOLHE TESOURA
    if jogador == 0:
        print('\033[1;32m Parabéns, você Ganhou ! ')
    elif jogador == 1:
        print('\033[1;31m haha, eu ganhei ! !')
    elif jogador == 2:
        print('\033[1;33m Empate, vamos novamente ? !')
    else:
        print('\033[1;33;40m Jogada INVÁLIDA! ')
else:
    print('1;33;40m Jogada INVÁLIDA!')