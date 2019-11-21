# Exercício Python 063: Escreva um programa que leia um número N inteiro
# qualquer e mostre na tela os N primeiros elementos de uma Sequência de
# Fibonacci. 

print('-' * 23)
print('Sequência de Fibonacci')
print('-' * 23)

n = int(input('Quantos termos você quer mostrar? '))

cont = 3
f1 = 0
f2 = 1
f3 = 0

print('~' * 30)
print('{} -> {} ->'.format(f1, f2), end='')

while cont <= n:
    f3 = f1 + f2
    print(' {} -> '.format(f3), end='')
    f1 = f2
    f2 = f3
    cont += 1
print('FIM')
