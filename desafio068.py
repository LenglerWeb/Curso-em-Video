# Exercício Python 068: Faça um programa que jogue par ou ímpar com o
# computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final
# do jogo.

print('=-' * 14)
print('VAMOS JOGAR PAR OU IMPAR ?')
print('=-' * 14)

n = cont = 0
pi = 'Pp', 'Ii'
while True:
    n = int(input('Escolha um número: '))
    if n == 0:
        break
    pi = str(input('PAR ou IMPAR? [P/I]: ')).upper().strip()[0]

print('FIM')
    
