# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print('Caixa de Mercado')
preco = float(input('Informe o valor do produto: R$'))

print('Escolha a forma de pagamento:')
print(' [ 1 ] - à vista dinheiro/cheque')
print(' [ 2 ] - à vista no cartão')
print(' [ 3 ] - em até 2x no cartão')
print(' [ 4 ] - 3x ou mais no cartão')

op = int(input('Informe a opção: [1 à 4] '))

if op == 1:
    novopreco = preco - (preco * (10 / 100))
    print('Valor de {:.2f} com 10"%" de desconto: R${:.2f}'.format(preco, novopreco))

elif op == 2:
    novopreco = preco - (preco * (5 / 100))
    print('Valor de {:.2f} com 5"%" de desconto: R${:.2f}'.format(preco, novopreco))

elif op == 3:
    novopreco = preco / 2
    print('Valor de {:.2f} em 2x no cartão de crédito: 1/2 de R${:.2f}'.format(preco, novopreco))

elif op == 4:
    n = preco + (preco * (20 / 100))
    parcela = int(input('Quantas parcelas: '))
    novopreco = ((preco + (preco * (20 / 100))) / parcela)
    print('Total com 20"%" de juros: R${:.2f}'.format(n))
    print('Valor de {:.2f} em 3x no cartão de crédito com 20"%" de juros: 1/3 de R${:.2f}'.format(preco, novopreco))

else:
    print('\033[7;31;40mOpção INVÁLIDA!\033[m')

