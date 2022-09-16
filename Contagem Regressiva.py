#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
print('\033[1;31;40m Vamos iniciar a contagem regressiva...\033[m')
from time import sleep
for e in range (10, 0, -1):
    sleep(1)
    print(e)
sleep(1)
print('\033[7;33;40m Feeeliz ano noooovo!\033[m')