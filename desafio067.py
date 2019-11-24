# Exercício Python 067: Faça um programa que mostre a tabuada de vários
# números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

t = 0
cont = 1

while True:
    print('#' * 30)
    t = int(input('Qual tabuada você quer saber? '))
    print('#' * 30)
    cont = 1

    if t <= 0:
        break
                
    while cont <= 10:
        print(f'{t} x {cont} = {t*cont}')
        cont += 1    
    
print('PROGRAMA DA TABUADA ENCERRADO!')
