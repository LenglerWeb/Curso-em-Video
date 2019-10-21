# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre 
# a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

print('Digite 6 números inteiros')
print('=' * 15)
s = 0
impar = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {} número: '.format(c)))
    if (n % 2) == 0:
        # s = n + s
        s += n
        # cont = cont + 1
        cont += 1
print('Foram {} número(s) par(es).'.format(cont))
print('A soma dos números pares: {}'.format(s))    



