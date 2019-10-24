# Exercício Python 056: Desenvolva um programa que leia o nome, 
# idade e sexo de 4 pessoas. No final do programa, 
# mostre: a média de idade do grupo, 
# qual é idade e o nome do homem mais velho e 
# quantas mulheres têm menos de 20 anos.

soma2 = 0
maior = 0
name = ''
for c in range(1, 5):
    print('\033[7;33;40m--- Digite a {}ª pessoa ---\033[m'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    #sexo = str(input('Sexo [M/F]: ')).upper()

    # Este laço realiza a média das idades!
    cont = idade
    soma2 += idade
    media = soma2 / 4
    
    # Este laço realiza a retenção da maior idade e do nome:
    if idade > maior and nome != '':
        maior = idade
        name = nome

    # Este laço realiza a soma de mulheres

print('-' * 25)
#print('soma {}'.format(soma2))
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, name))

