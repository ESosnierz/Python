vhora = float(input('Informe o valor de sua hora: '))
qhora = float(input('Informe a quantidade de hora no mês: '))
sbruto = vhora * qhora
inss = (sbruto * 10) / 100
sind = (sbruto * 3) / 100
fgts = (sbruto * 11) / 100

if (sbruto <= 900):
    print('Seu Salário bruto é de R$ ', sbruto)
    print('(-) IR : Isento')
    print('(-) INSS (10%): R$ {}'.format(inss))
    print('(-) Sindicato (3%): R$ {}'.format(sind))
    print('FGTS (11%): R$ {}'.format(fgts))
    desconto = inss + sind
    print('Total de desconto: R$ {}'.format(desconto))
    sliquido = (sbruto - desconto)
    print('Salário Líquido: R$ {}'.format(sliquido))
elif (sbruto <= 1500):
    print('Seu Salário bruto é de R$ ', sbruto)
    ir = (sbruto * 5) / 100
    print('(-) IR (5%) : R$ {}'.format(ir))
    print('(-) INSS (10%): R$ {}'.format(inss))
    print('(-) Sindicato (3%): R$ {}'.format(sind))
    print('FGTS (11%): R$ {}'.format(fgts))
    desconto = inss + sind + ir
    print('Total de desconto: R$ {}'.format(desconto))
    sliquido = (sbruto - desconto)
    print('Salário Líquido: R$ {}'.format(sliquido))
elif (sbruto <= 2500):
    print('Seu Salário bruto é de R$ ', sbruto)
    ir = (sbruto * 10) / 100
    print('(-) IR (10%): R$ {}'.format(ir))
    print('(-) INSS (10%): R$ {}'.format(inss))
    print('(-) Sindicato (3%): R$ {}'.format(sind))
    print('FGTS (11%): R$ {}'.format(fgts))
    desconto = inss + sind + ir
    print('Total de desconto: R$ {}'.format(desconto))
    sliquido = (sbruto - desconto)
    print('Salário Líquido: R$ {}'.format(sliquido))
else:
    print('Seu Salário bruto é de R$ ', sbruto)
    ir = (sbruto * 20) / 100
    print('(-) IR (20%): R$ {}'.format(ir))
    print('(-) INSS (10%): R$ {}'.format(inss))
    print('(-) Sindicato (3%): R$ {}'.format(sind))
    print('FGTS (11%): R$ {}'.format(fgts))
    desconto = inss + sind + ir
    print('Total de desconto: R$ {}'.format(desconto))
    sliquido = (sbruto - desconto)
    print('Salário Líquido: R$ {}'.format(sliquido))