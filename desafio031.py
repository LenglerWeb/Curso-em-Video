#031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
# e R$0,45 parta viagens mais longas.

d = int(input('Qual a distância em Km, da sua viagem: '))
if d <= 200:
    print('O valor total da sua passagem: R${:.2f}'.format(d * 0.5))
else:
    print('O valor total da sua passagem: R${:.2f}'.format(d * 0.45))