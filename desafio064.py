# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um número inteiro qualquer [999 para sair]: '))
    soma = soma + n
    cont += 1
# minha ideia foi esta abaixo, a do professor foi colocar dentro do .format => .format(cont -1, soma - 999).
soma = soma - 999
cont -= 1     
print('Foram digitados {} números e a soma total foi {}.'.format(cont, soma))

##################################################
# Abaixo foi a resolução que o professor passou: #
##################################################
# n = cont = soma = 0
# n = int(input('Digite um número inteiro qualquer [999 para sair]: '))
# while n != 999:
#     soma += n
#     cont += 1
#     n = int(input('Digite um número inteiro qualquer [999 para sair]: '))
# print('Foram digitados {} números e a soma total foi {}.'.format(cont, soma))    