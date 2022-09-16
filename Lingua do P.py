curso = input('Diga sua frase e falaremos na lingua do P:')
for i in curso:
    if i=='a' or i =='e' or i=='i' or i=='o' or i=='u':
        print(i+'p'+i, end='')
    else:
        print(i, end='')