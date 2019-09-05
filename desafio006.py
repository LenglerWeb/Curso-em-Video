# crie um algorítmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada:

n = int(input('Digite um numero para descobrir o seu dobro, triplo e sua raiz quadrada: '))
print('O dobro de {} é {}'.format(n, n*2))
print('O triplo de {} é {}'.format(n, n*3))
print('A raiz quadrada de {} é {:.2f}'.format(n, n ** (1/2)))
print('Raiz Quadrada utilizando a "função pow()" é {:.2f}'.format(pow(n, (1/2))))
