# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai
# "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites foram necessários
# para vencer.

from random import randint
print('Sou seu computador...')
npc = randint(0,10)
print('Pensei em um número entre 0 à 10.')
print('Será que você consegue adinhvinhar qual foi?')
cont = 1
n = int(input('Qual é o seu palpite? '))

while n != npc:
    n = int(input('Qual é o seu palpite? '))
    cont += 1
print('PARABÉNS! Você acertou com {} tentativas.'.format(cont))
print('FIM')
