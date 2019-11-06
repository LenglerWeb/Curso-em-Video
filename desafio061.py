# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a 
# razão de uma PA, mostrando os 10 primeiros termos da progressão usando a 
# estrutura while.

print('=-' * 17)
print('Calcular o FATORIAL de um número.')
print('=-' * 17)
n = int(input('Digite um número inteiro: '))
c = n
f = 1

print('{}! = '.format(n), end='')
for c in range(c, 0, -1):
    print('{}'.format(n), end='')
    if c == 1:
        print(' = ', end='')
    else:
        print(' x ', end='')
    n -= 1
    f *= c
print('{}'.format(f))
print('\nFIM do Exemplo 3.')
