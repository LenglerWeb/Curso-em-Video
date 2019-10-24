# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não 
# um número primo.

n = int(input('Digite um número inteiro: '))

print('Divisão inteira de {} = {}'.format(n, n // n))
# Divisão inteira de 1 = 3
print('O resto de {} = {}'.format(n, n % n))
# O resto de 1 = 0
#print('Divisão inteira de {} = {}'.format(n, n // n))
# Divisão inteira de 2 = 1
#print('O resto de {} = {}'.format(n, n % n))
# Divisão inteira de 2 = 1

for c in range(1, 3):
    if n % 1 != 1 and n % n != 0:
        print("OK")
    else:
        print('NÃO')

