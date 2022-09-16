
#----------------- Incluindo funções do programa!
#----------------- Brincando com agenda telefonica.

#----------------- [1] - Função para incluir um novo contato
def incluirNovoNome (agenda, novoNome, novosTelefones):
    agenda[novoNome] = novosTelefones
    print(f'\n>>> {nome} cadastrado com sucesso. ')
    
#----------------- [2] - Função para incluir novo número em existentes    
def incluirTelefone(agenda, nome, novoTelefone):
    fones = agenda[nome]
    fones.append(novoTelefone)
    agenda[nome] = fones
    print(f'\n>>> Telefone {novoTelefone} incluido.')
    
#----------------- [3] - Função para excluir apenas um número   
def excluirTelefone(agenda, nome, foneExcluido):
    agenda[nome].remove(foneExcluido)
    print(f'\n>>> Telefone {foneExcluido} removido com sucesso de {nome}.')
    

#----------------- [4] - Função para excluir o contato    
def excluirNome(agenda, nome):
    agenda.pop(nome)
    print(f'\n>>> Nome {nome} removido com sucesso.')

#----------------- [5] - Função para procurar contato na agenda    
def consultarTelefone(agenda, pessoa):
    print('\n>>> Início da agenda de telefones<<<')
    print(f'{pessoa} Fone: {agenda[pessoa]}')
    print('\n>>> Fim da Agenda de Telefones')

    
from time import sleep #incluindo tempo de retardo para a função

#----------------- Introdução
print('=-'*15)
print('     Agenda de Telefones')
print('=-'*15)
print('')

#----------------- Indicação da variavel
opcao = 0
dados = {'João':[111,222], 'Maria':[888,999]} #entrando com dicionário para agenda
#----------------- Iniciando o laço
while True: # emtrando no loop
    print('''
    \033[1;30;41mEscolha uma das opções: \033[m
    \033[33m      
    [1] - Incluir um novo contato
    [2] - Incluir novo número em existentes
    [3] - Excluir apenas um número
    [4] - Excluir o contato
    [5] - Procurar contato na agenda
    [6] - Sair\033[m    ''')
    print('=-'*15)
    opcao = int(input('Escolha uma das opções: '))
#----------------- [1] - Incluir um novo contato
    if (opcao == 1):        
        nome = str(input('Olá, Digite o nome: '))
        fones = []
        while True:
            tel = int(input('Agora digite o número: [digite (0) para encerar] '))
            if (tel == 0):
                break
            fones.append(tel)
        incluirNovoNome(dados, nome, fones)
        
#----------------- [2] - Incluir novo número em existentes
    elif (opcao == 2):
        nome = input('Informe o novo nome da pessoa: ')
        fone = int(input('Informe o telefone: '))
        incluirTelefone(dados, nome, fone)
        
#----------------- [3] - Excluir apenas um número
    elif (opcao == 3):
        nome = input('Informe o novo nome da pessoa: ')
        fone = int(input('Informe o telefone a ser excluido: '))
        excluirTelefone(dados, nome, fone)
        
#----------------- [4] - Excluir o contato
    elif (opcao == 4):
        nome = input('Informe o novo nome da pessoa a ser excluida: ')
        excluirNome(dados, nome)
        
#----------------- [5] - Procurar contato na agenda
    elif (opcao == 5):
        nome = input('Informe o nome a ser consultado: ')
        consultarTelefone(dados, nome)
        sleep(3)
        
#----------------- [6] - Sair
    elif (opcao == 6):
        print('\033[1;30;41mSaindo...\033[m')
        print('\033[31m3')
        sleep(1)
        print('2')
        sleep(1)
        print('1\033[m')
        sleep(1)
        break
    
#----------------- [Opção invalida]
    else:
        print('Opção Invalida, Escolha umas das opções informada!')
        continue
print('Obrigado, até breve')