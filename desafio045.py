# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('-= JOKENPÔ =-')
print('Escolha uma opção:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
escolha = int(input('Qual a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)

npc = randint(0,2)

print('Computador jogou {}'.format(itens[npc]))
print('Você escolheu {}'.format(itens[escolha]))

if escolha == 0 and npc == 2:
    print('\033[7;32;40mJogador Venceu!\033[m')
elif escolha == 1 and npc == 0:
    print('\033[7;32;40mJogador Venceu!\033[m')
elif escolha == 2 and npc == 1:
    print('\033[7;32;40mJogador venceu\033[m')

elif npc == 0 and escolha == 2:
    print('\033[7;31;40mComputador Venceu!\033[m')
elif npc == 1 and escolha == 0:
    print('\033[7;31;40mComputador Venceu!\033[m')
elif npc == 2 and escolha == 1:
    print('\033[7;31;40mComputador Venceu!\033[m')
else:    
    print('\033[7;33;40mEMPATE!\033[m')
    