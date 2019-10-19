# Exercício Python 048: Faça um programa que calcule a soma entre todos os números 
# impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        s = s + c
        cont = cont + 1
print('\n')
print('Total de números múltiplos de 3: \033[7;32;40m{}\033[m'.format(cont))
print('A soma de todos os {} números: \033[7;32;40m{}\033[m'.format(cont, s))
