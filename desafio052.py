# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é 
# ou não um número primo.

num = int(input('Digite um número inteiro: '))
total = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[1;36m', end='')
        total += 1
    else:
        print('\033[1;31m', end='')
    print('{}'.format(c), end=' ')
print(' \033[m')
print('O número {} foi disível {} vezes.'.format(num, total))
