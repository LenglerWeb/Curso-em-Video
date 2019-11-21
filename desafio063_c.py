num = int(input('Digite um número de termo para sequência Fibonacci: '))

cont = 1
f1 = 0
f2 = 1
soma = 1

while cont <= num:

     print(f1, end='-')
     cont += 1
     soma = f2 + f1
     f1 = f2
     f2 = soma

print('Fim')
