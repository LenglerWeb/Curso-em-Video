# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

# Exemplo 1:
from math import factorial
print('=-' * 17)
print('Calcular o FATORIAL de um número.')
print('=-' * 17)


n = int(input('Digite um número inteiro: '))
f = factorial(n)

print('O fatorial de {}! é {}'.format(n, f))
print('FIM do Exemplo 1.')

# Exemplo 2:
print('\n')

print('=-' * 17)
print('Calcular o FATORIAL de um número.')
print('=-' * 17)
n = int(input('Digite um número inteiro: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    if c > 1:
        print(' x ', end='')
    else: 
        print(' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
print('\nFIM do Exemplo 2.')


# Exemplo 3 com for:
print('\n')

print('=-' * 17)
print('Calcular o FATORIAL de um número.')
print('=-' * 17)
n = int(input('Digite um número inteiro: '))
c = n
f = 1

print('{}! = '.format(n), end='')
for c in range(c, 0, -1):
    print('{}'.format(n), end='')
    if c == 1:
        print(' = ', end='')
    else:
        print(' x ', end='')
    n -= 1
    f *= c
print('{}'.format(f))
print('\nFIM do Exemplo 3.')