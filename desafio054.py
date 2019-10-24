# Exercício Python 054: Crie um programa que leia o ano de 
# nascimento de sete pessoas. No final, mostre quantas 
# pessoas ainda não atingiram a maioridade e quantas já 
# são maiores.

ano = 0
adulto = 0
jovem = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu: '.format(c)))

    if ano >= 2002:
        jovem += 1
    else:
        adulto += 1
print('\nAo todo tivemos {} pessoas maiores de idade.'.format(adulto))
print('E também tivemos {} pessoas menores de idade.'.format(jovem))
