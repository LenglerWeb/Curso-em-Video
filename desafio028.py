#028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
n = int(input('Digite um número entre 0 e 5 e tente adivinhar qual número o PC pensou: '))
npc = randint(0,5)
if n == npc:
    print('PARABÉNS!!! Você acertou.')
else:
    print('Você ERROU!!! Eu pensei no número {}. Tente novamente.'.format(npc))