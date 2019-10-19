# Estrutura de REPETIÇÃO
##############################
# laço c no intervalo(1, 10)
#   passo
# pega
##############################
# for c in range(1, 10):
#   passo
# pega
##############################
# laço c no intervalo(0, 3)
#   passo
#   pula
# passo
# pega
##############################
# for c in range(0, 3):
#   passo
#   pula
# passo
# pega
###############################
# laço c no intervalo(0, 3)
#   se moeda
#       pega
#   passo
#   pula
# passo
# pega
################################
# for c in range(0, 3):
#   if moeda:
#       pega
#   passo
#   pula
# passo
# pega
################################
print('Executa Passo e Pula 3 vezes e sai do laço e executa o resto do programa:')
for c in range(0, 3):
    print('\033[7;33;40mexecução\033[m {}'.format(c))
    print('Passo')
    print('Pula')
print('\033[7;33;40mSaiu do laço para continuar o resto do programa!\033[m')
print('Ultimo Passo')
print('Pega')
print('#' * 14)
##############################
print('Conta de 0 até 5:')
for c in range(0, 6):
    print(c)
print('FIM')
print('#' * 14)
##############################
print('Conta de 1 até 6:')
for c in range(1, 7):
    print(c)
print('FIM')
print('#' * 14)
##############################
print('Contagem regressiva:')
for c in range(6, 0, -1):
    print(c)
print('FIM')
print('#' * 14)
###############################
print('Pula de 2 em 2:')
for c in range(0, 7, 2):
    print(c)
print('FIM')
print('#' * 14)
###############################
print('Escolhendo quantas vezes executar o laço:')
n = int(input('Digite um número inteiro para contar até ele: '))
for c in range(0, n + 1):
    print(c)
print('FIM')
print('#' * 14)
################################
i = int(input('Digite o número de Início: '))
f = int(input('Informe o número de Fim: '))
p = int(input('Quantos Passos: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
print('#' * 14)
##################################
for c in range(0, 3):
    n = int(input('Digite um número inteiro: '))
print('FIM')
print('#' * 14)
##################################
print('SOMAR 3 números:')
s = 0
for c in range(0, 3):
    n = int(input('Digite um número: '))
    s += n
print('A soma dos números: {}'.format(s))
print('#' * 14)
###################################
