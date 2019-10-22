# minha tentativa de refazer o desafio052.py

n = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[1;32mSIM -> ', end=' ')
        cont += 1
    else:
        print('\033[1;31mNão -> ', end=' ')
    print('{}\033[m,'.format(c), end=' ')
  
print('-> FIM')
print('O número {} foi disivível {} vezes.'.format(n, cont))

if cont == 2:
    print('\033[1;32mO número {} é PRIMO!\033[m'.format(n))
else:
    print('\033[1;31mO número {} NÃO é PRIMO!\033[m'.format(n))
