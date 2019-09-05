# O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos.
# faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada:

import random
# from random import shuffle
nome1 = input('Primeiro nome: ')
nome2 = input('Segundo nome: ')
nome3 = input('Terceiro nome: ')
nome4 = input('Quarto nome: ')

lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
# shuffle(lista)
print('A ordem de apresentação é: {}'.format(lista))
