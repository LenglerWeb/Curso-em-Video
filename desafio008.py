# escreva um programa que leia um valor em METROS e o exiba convertido em centímetros e milímetros:

m = int(input('Quantos METROS? '))
c = m * 100
mi = m * 1000
print('{} metros convertido para CENTÍMETROS: {}'.format(m, c))
print('{} metros convertido para MILÍMETROS: {}'.format(m, mi))