# Exercício Python 057:
# Faça um programa que leia o sexo de uma pessoa, mas só
# aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter
# um valor correto.

'''r = 'S'
while r == 'S':
    n = int(input('Digite um número inteiro: '))
    r = str(input('Quer continuar? [S/N]')).strip().upper()
print('FIM')'''

sair = ''
sexo = ''
print('Para SAIR do programa digite "S".')
while sair != 'S':
    sexo = str(input('Informe o seu sexo: [M/F]: ')).strip().upper()[0]
    # while sexo != 'M' and sexo != 'F':
    while sexo not in 'MmFf':
        sexo = str(input('ERRO! Digite novamente o seu sexo: [M/F]: ')).strip().upper()[0]
    print('Sexo {} registrado com SUCESSO.'.format(sexo))
    

    sair = str(input('Deseja sair? [S/N]: ')).strip().upper()
    while sair != 'S' and sair != 'N':
        sair = str(input('ERRO! Digite somente [S/N]: ')).strip().upper()
        
      
print('FIM')

