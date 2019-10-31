# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai
# "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites foram necessários
# para vencer.

from random import randint
print('Sou seu computador...')
npc = randint(0,10)
print('Pensei em um número entre 0 à 10.')
print('Será que você consegue adivinhar qual foi?')
cont = 0
n = 11

while n != npc:
    n = int(input('Qual o seu palpite? '))
    cont += 1
    if n < npc:
        print('Tente um número maior!')

    elif n > npc:
        print('Tente um número menor!')
    
        
print('PARABÉNS! Você acertou com {} tentativa(s).'.format(cont))
print('FIM')

##############################################################
# Solução do professor!
##############################################################
# palpite = 0
# acertou = False
# while not acertou:
#    jogador = int(input('Qual o seu palpite? '))
#    palpite += 1
#    if jogador = npc:
#        acertou = True
#    else:
#        if jogador < npc:
#            print('Mais... Tente mais uma vez.')
#        elif jogador > npc:
#            print('Menos... Tente mais uma vez.')
# print('Parabéns! Você acertou com {} tentativas.'.format(palpite))
##############################################################