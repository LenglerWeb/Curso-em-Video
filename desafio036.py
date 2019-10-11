# 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

vcasa = float(input('Qual o valor da casa que deseja comprar: R$'))
salario = float(input('Qual o salário do comprador: R$'))
qdata = int(input('Em quantos anos de empréstimo: '))
meses = qdata * 12
prestacao = vcasa / meses
liberacao = salario * (30 / 100)

if liberacao > prestacao:
    print('Empréstimo {}{}{}'.format('\033[1;35m', 'LIBERADO!!!', '\033[m'))
    print('Total de {}{}{} meses de prestação.'.format('\033[1;35m', meses, '\033[m'))
    print('Valor de cada prestação: {}R${:.2f}{}'.format('\033[1;35m',prestacao, '\033[m'))
else:
    print('Em {} meses.'.format(meses))
    print('Valor da prestação: R${:.2f}'.format(prestacao))
    print('Valor dos 30"%" do salário: R${}'.format(liberacao))
    print('Empréstimo {}{}{}'.format('\033[1;31;40m', 'NEGADO!!','\033[m'))