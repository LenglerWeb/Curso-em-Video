# Exercício Python 057:
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M'
# ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

'''sair = 'S'
sexo = ''
print('Para SAIR do programa digite "S".')
while sair == 'S':
    sexo = str(input('Informe o seu sexo: [M/F]: ')).strip().upper()
    sair = str(input('Deseja sair? [S/N]: ')).strip().upper()
print('FIM')'''

r = 'S'
while r == 'S':
    n = int(input('Digite um número inteiro: '))
    r = str(input('Quer continuar? [S/N]')).strip().upper()
print('FIM')
               
    
