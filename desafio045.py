# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
itens = ('Pedra', 'Papel', 'Tesouras')
print('-= JOKENPÔ =-')
print('Escolha uma opção:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
escolha = int(input('Qual a sua jogada? '))

print('JO')
print('KEN')
print('PÔ!!!')
npc = randint(0,2)

print('Computador jogou {}'.format(itens[npc]))
print('Você escolheu {}'.format(itens[escolha]))

if escolha == 0 and npc == 2:
    print('Jogador Venceu!')
elif escolha == 1 and npc == 0:
    print('Jogador Venceu!')
elif escolha == 2 and npc == 1:
    print('Jogador venceu')

elif npc == 0 and escolha == 2:
    print('Computador Venceu!')
elif npc == 1 and escolha == 0:
    print('Computador Venceu!')
elif npc == 2 and escolha == 1:
    print('Computador Venceu!')
else:    
    print('\033[7;33;40mEMPATE!\033[m')
    