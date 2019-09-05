# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. # Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Informe a quantidades KM reodados: '))
dias = int(input('Informe quantos DIAS de alugel: '))
valordia = dias * 60
kmrodado = km * 0.15
print('O valor da diária R$ {:.2f}'.format(valordia))
print('O valor da Kilometragem Rodada R$ {:.2f}'.format(kmrodado))
print('Total para pagamento R$ {:.2f}'.format(valordia + kmrodado))