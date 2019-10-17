# 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de 
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date

ano = int(input('Qual o ano de nascimento do atleta: '))
anoatual = date.today().year
#anoatual = 2019
idade = anoatual - ano

if idade > 25:
    print('O atleta tem {} anos e é \033[7;33;40mMASTER\033[m'.format(idade))

# elif idade <= 25:
elif idade >= 20 and idade <= 25:
    print('O atleta tem {} anos e é \033[7;33;40mSÊNIOR\033[m'.format(idade))

# elif idade <= 19:
elif idade >= 15 and idade < 20:
    print('O atleta tem {} anos e é \033[7;33;40mJÚNIOR\033[m'.format(idade))
# elif idade <= 14:
elif idade >= 10 and idade < 15:
    print('O atleta tem {} anos e é \033[7;33;40mINFANTIL\033[m'.format(idade))
# elif idade <= 9:
elif idade < 10:
    print('O atleta tem {} anos e é \033[7;33;40mMIRIM\033[m'.format(idade))
