#################################################
# Curso Python3 -> Laços de Repetição (parte 2) #
#################################################
#
# OBS MUITO IMPORTANTE:
# O comando WHILE serve tanto para quanso se sabe o limite de vezes que se deve executar uma açao
# como quando não se sabe quantas vezes uma ação deve ser executada!
##################################################################################################

# enquanto não chegar na maçã
#   passo
# pega

# while not maçã:
#   passo
# pega

#################################################

# enquanto não maçã
#   se tiver chão
#       passo
#   se tiver buraco
#       pulo
#   se tiver moeda
#       pega
# pega


# while not maçã:
#   if chão:
#       passo
#   if buraco:
#       pulo
#   if moeda:
#       pega
# pega

##################################################

# Aula anterior com FOR
'''for c in range(1, 10):
    print(c, end=' ')
print('FIM')'''

# O mesmo só que com WHILE
c = 1
while c < 10:
    print(c, end=' ')
    c += 1
print ('FIM')

# Com FOR
print('=' * 25)
'''for c in range(1, 3):
    n = int(input('Digite um número: '))
print('FIM')'''

# Com WHILE (o comando para quando informado o número "0"
n = 1
print('Para sair digite "0".')
while n != 0:
    n = int(input('Digite um número: '))
print('FIM')

# Outro exemplo:
r = 'S'
while r == 'S':
    n = int(input('Digite um número inteiro: '))
    r = str(input('Quer continuar? [S/N]')).strip().upper()
print('FIM')
        
# Parar de informar um número quando digitado "0" para saber quantos números
# são PAR ou IMPAR:
n = 1
par = impar = 0
print('Para sair digite "0" e saber quantos são PAR.')
while n != 0:
    n = int(input('Digite um número inteiro: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Foram digitados \033[7;33;40m{}\033[m números PAR e \033[7;31;40m{}\033[m números IMPAR.'.format(par, impar))
print('ACABOU')  
