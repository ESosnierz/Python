print('\033[31mOlá, mundo!')
print('\033[1;35;40mOlá, mundo!')
print('\033[1;35;40mOlá, mundo!\033[m')
print('\033[4;30;45mOlá, mundo!\033[m')
print('\033[1;30;41mOlá, mundo!\033[m')
print('\033[7;37mOlá, mundo!\033[m')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a,b))
print('Os valores são \033[32;47m{}\033[m e \033[31;47m{}\033[m'.format(a,b))
nome= 'Elson'
print('Olá, muito prazer em te conhecer, {}{}{} !!!'.format('\033[4;34m', nome, '\033[m'))
nome= 'Elson'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}
print('Olá, muito prazer em te conhecer, {}{}{} !!!'.format(cores['amarelo'], nome, cores['limpa']))
print('Olá, muito prazer em te conhecer, {}{}{} !!!'.format(cores['azul'], nome, cores['limpa']))
print('Olá, muito prazer em te conhecer, {}{}{} !!!'.format(cores['pretoebranco/'], nome, cores['limpa']))
