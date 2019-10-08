# 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário 
# se elas podem ou não formar um triângulo.

print('Digite 3 valores para verificar se eles formam um triângulo ou não:\n')
a = float(input('Informe o tamanho da primeira reta: '))
b = float(input('Informe o tamnaho para a segunda reta: '))
c = float(input('Informe o tamanho para a terceira reta: '))

if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('OK, os 3 segmentos de retas formam um triângulo')
else:
    print('NÃO, infelizmente os 3 segmentos informados NÃO formam um triângulo')
