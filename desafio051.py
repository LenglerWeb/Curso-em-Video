# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#  No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 51)
print(' 10 primeiros termos de uma Progressão Aritmética: ')
print('=' * 51)

a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a Razão: '))

# d é a variável décimo termo.
d = a + (11 - 1) * r

for c in range(a, d, r):
    
    print('{}'.format( c ), end=' -> ')

print('FIM')
