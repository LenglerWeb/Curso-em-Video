# Exercício Python 056: Desenvolva um programa que leia o nome, 
# idade e sexo de 4 pessoas. No final do programa, 
# mostre: a média de idade do grupo, 
# qual é idade e o nome do homem mais velho e 
# quantas mulheres têm menos de 20 anos.

soma = 0
maior = 0
name = ''
mulheres = 0
for c in range(1, 5):
    print('--- Digite a {}ª pessoa ---'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    # Este laço realiza a média das idades!
    
    soma += idade
    media = soma / 4
    
    # Este laço realiza a retenção da maior idade e do nome:
    if idade > maior and nome != '':
        if sexo == 'M':
            maior = idade
            name = nome
        
    # Este laço realiza a soma de mulheres
    if sexo == 'F' and idade < 20:
        mulheres += 1

print('-' * 25)
#print('soma {}'.format(soma))
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, name))
print('Ao todo são {} mulher(es) com menos de 20 anos.'.format(mulheres))
