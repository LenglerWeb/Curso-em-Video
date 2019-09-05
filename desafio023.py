#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = input('Digite um numero entre 0 e 9999: ')
separado = num
#separado = ' '.join(num)
uni = separado[3]
dez = separado[2]
cen = separado[1]
mil = separado[0]
print(separado)

print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cen))
print('Milhar: {}'.format(mil))
separado = ' '.join(num)
print('Os numeros separados: ', separado)