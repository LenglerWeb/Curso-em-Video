# minha versão do programa do FIBONACCI - desafio063_b.py

print('=~=' * 10)
print('Sequência de FIBONACCI')
print('=~=' * 10)

n = int(input('Informe quantos termos deve mostrar: '))

# cont inicia em 3 porque já foi mostrado o f1 e o f2!!
cont = 3
f1 = 0
f2 = 1
f3 = 0

print('{} -> {} '.format(f1, f2), end='')

while cont <= n:
    
    f3 = f1 + f2
    print('-> {} '.format(f3), end='')
    f1 = f2
    f2 = f3
    cont += 1

print('-> FIM')
