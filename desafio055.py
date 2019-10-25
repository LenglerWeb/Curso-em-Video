# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.


maior = 0.0
menor = 0.0

for c in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('O \033[1;32mmaior peso\033[m informado foi: \033[1;32m{}\033[mKg'.format(maior))
print('O \033[1;33mmenor peso\033[m informado foi: \033[1;33m{}\033[mKg'.format(menor))
