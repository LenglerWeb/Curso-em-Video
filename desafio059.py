# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu 
# na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
op = 0
while not op == 5:
    
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    
    op = int(input('>>>> Opção: '))

    if op == 1:
        soma = n1 + n2
        print('A soma de {} + {} = {}'.format(n1, n2, soma))
        print('=-' * 15)
        sleep(1)
    elif op == 2:
        multiplicar = n1 * n2
        print('A multiplicação de {} * {} = {}'.format(n1, n2, multiplicar))
        print('=-' * 15)
        sleep(1)
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número foi o {}.'.format(maior))
        print('=-' * 15)
        sleep(1)
    elif op == 4:
        print('Informe dois novos números.')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
        print('=-' * 15)
        sleep(1)
    else:
        print('Opção Inválida, tente novamente.')
        print('=-' * 15)
        sleep(1)
print('FIM')
