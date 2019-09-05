# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
# ex.: Digite um numero: 6.127
# O numero 6.127 tem a parte inteira 6

from math import trunc
num = float(input('Digite um numero REAL: '))
#print('A parte inteira de {} é {:.0f}'.format(num, num))
#print('A parte inteira de {} é {}'.format(num, int(num))
print('A parte interira de {} é {}'.format(num, trunc(num)))
# Solução retirada dos comentários da aula:
#num = float(input('Digite um número qualquer'))
#print(f'A parte inteira de {num} é {trunc(num)}')
