# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

print('=-' * 17)
print('Calcular o FATORIAL de um número.')
print('=-' * 17)

f = 0
n = int(input('Digite um número inteiro: '))

while not n == 1:
    f = n * (n - 1)
    n -= 1
    
    #soma = f * n
      
   

    #print('o n = {}'.format(n))
    print('o f = {}'.format(f))
    #print('a SOMA = {}'.format(soma))
    print('-' * 9)
print('Total = {}'.format(f))
print('FIM')