# Um professor quer sortear um de seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do
# escolhido:

import random
# from random import choice
aluno1 = input('Informe o nome do aluno(a): ')
aluno2 = input('Informe o nome do segundo aluno(a): ')
aluno3 = input('Informe o nome do terceiro aluno(a): ')
aluno4 = input('Informe o nome do quarto aluno(a): ')

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
# escolhido = choice(lista)
print('O aluno(a) escolhido é {}'.format(escolhido))
