<<<<<<< HEAD
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

=======
# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é 
# ou não um número primo.

num = int(input('Digite um número inteiro: '))
total = 0
for c in range(1, num+1):
    if num % c == 0:
        # Se o número for PRIMO
        print('\033[1;36m', end='')
        total += 1
    else:
        # Se o número NÃO for PRIMO
        print('\033[1;31m', end='')
    
    print('{}'.format(c), end=' ')
    
print(' \033[m')
print('=' * 30)
print('\nO número {} foi disível {} vezes.'.format(num, total))

if total == 2:
    # Se o número for divisível APENAS 2 VEZES ele É PRIMO
    print('O número {} é \033[7;32;40mPRIMO!!\033[m'.format(num))
else:
    print('O número {} \033[7;31;40mNÃO É PRIMO\033[m'.format(num))
>>>>>>> e1abc9d9c76f14f433c288532253a28ffaee63c0
