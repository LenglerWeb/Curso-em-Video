# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a 
# razão de uma PA, mostrando os 10 primeiros termos da progressão usando a 
# estrutura while.

print('=' * 51)
print(' 10 primeiros termos de uma Progressão Aritmética: ')
print('=' * 51)

n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a Razão: '))
pa = n + (11 - 1) * r
c = n

while c < pa:
    print('{}'.format(c), end='')
    if c == pa - r:
        print('.')
    else:
        print(end=' -> ')
    c += r

print('FIM')

########################################
#        Resolução do professor:       #
########################################
# print('=' * 51)
# print(' 10 primeiros termos de uma Progressão Aritmética: ')
# print('=' * 51)
# n = int(input('Digite o primeiro termo: '))
# razão = int(input('Digite a razão: '))
# termo = n
# cont = 1
# while cont <=10:
#   print('{} -> '.format(termo), end=''))
#   termo += razão
#   cont += 1
# print('FIM')
