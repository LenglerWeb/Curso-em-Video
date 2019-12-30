# Exercício Python 068: Faça um programa que jogue par ou ímpar com o
# computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final
# do jogo.

from random import randint

print('=-' * 14)
print('VAMOS JOGAR PAR OU IMPAR ?')
print('=-' * 14)

cont = 0

while True:
    resultado = 0
    pi = ' '
    
    n = int(input('Escolha um número: '))
    computador = randint(1, 5)
    resultado = n + computador
    
    while pi not in 'PI':
        pi = str(input('PAR ou IMPAR? [P/I]: ')).upper().strip()[0]
           
    print(f'O Computador escolheu: {computador}')
    
    if pi == 'P':
        if resultado % 2 == 0:
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    
    elif pi == 'I':
        if resultado % 2 == 1:
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
        
    print('Vamos jogar nomevente!')
print(f'Você venceu {cont} vezes seguidas.')

    
