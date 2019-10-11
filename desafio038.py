#038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela 
# uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O \033[1;35mprimeiro\033[m número é MAIOR!')
elif n2 > n1:
    print('O \033[1;36msegundo\033[m número é MAIOR!')
else:
    print('Os \033[1;33mdois\033[m números são IGUAIS!')