# Faça um algoritmo que leia o salário de um funcionário e mostre o novo salário com 15% de aumento:

sal = float(input('O salário atual do funcionário: R$ '))
aument = sal * (15 / 100)
novosal = sal + aument
print('O novo salário do funcionário com 15% de aumento: R$ {:.2f}'.format(novosal))