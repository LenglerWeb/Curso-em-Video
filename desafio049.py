# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, 
# só que agora utilizando um laço for.

n = int(input('Digite o número para descobrir a sua tabuada: '))
print('=' * 13)
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n * c))
print('=' * 13)

