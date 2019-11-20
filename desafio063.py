# Exercício Python 063: Escreva um programa que leia um número N inteiro
# qualquer e mostre na tela os N primeiros elementos de uma Sequência de
# Fibonacci. 

print('-' * 23)
print('Sequência de Fibonacci')
print('-' * 23)

n = int(input('Quantos termos você quer mostrar? '))
termo = n
cont = 1
f = 0
s = 0
while cont <= termo:
    print('{} -> '.format(s), end='')
    f1 = 1
    s = f + f1
    
    cont += 1
print('FIM')
