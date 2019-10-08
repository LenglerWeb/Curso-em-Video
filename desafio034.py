# 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do 
# seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe o salário do funcionário: R$'))
if salario > 1250:
    nsalario = (salario * 10) / 100
    print('O funcionário terá 10"%" de aumento, o novo salário é de R${:.2f}'.format(salario + nsalario))
else:
    nsalario = (salario * 15) / 100
    print('O funcionário terá 15"%" de aumento, seu novo salário é de R${:.2f}'.format(salario + nsalario))