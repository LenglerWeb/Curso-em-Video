#  029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Qual a velocidade atual do carro? '))
m = (v - 80) * 7

if v > 80:
    print('Você excedeu o limite de velocidade de 80Km/h, e foi MULTADO!!!')
    print('O valor da sua multa é de: R${:.2f}'.format(m))
else: 
    print('Você está dentro do limite de velocidade, continue assim.')