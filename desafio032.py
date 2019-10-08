# 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Informe um ano que deseja consultar: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} É bissexto'.format(ano))
else:
    print('O ano {} NÃO É bissexto'.format(ano))
