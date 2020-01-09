'''
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint

print('Foi sorteado os números: ', end='')
random = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for n in random:
    print(f'{n} ', end='')
print('')
#print(random)
print(f'O MAIOR número sorteado foi: {max(random)}')
print(f'O MENOR número sorteado foi: {min(random)}')