# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário
# se ele quer mostrar mais alguns termos. O programa encerrará quando ele
# disser que quer mostrar 0 termos.

print('*=*' * 18)
print('Os 10 primeiros termos de uma Progressão Aritmética:')
print('Para sair do programa digite "0".')
print('*=*' * 18)

n = int(input('Digite o primeiro Termo: '))
r = int(input('Digite a Razão: '))

pa = n 
cont = 1
mais = 10
total = 0

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(pa), end='')
        if cont == 10:
            print('.')                
        else:
            print(end=' -> ')
        pa += r
        cont += 1

    print('PAUSA')
    mais = int(input('Quantos termos mais você quer mostrar? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

