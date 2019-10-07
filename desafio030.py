#030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número para saber se ele é PAR ou IMPAR: '))
r = n % 2 

if n == 0:
    print('O número 0 NÃO É par ou impar!')
elif r == 0:
    print('O número {} é PAR.'.format(n))
else:
    print('O número {} é IMPAR.'.format(n))