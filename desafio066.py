# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a
# condição de parada. No final, mostre quantos números foram digitados e
# qual foi a soma entre elas (desconsiderando o flag).

n = soma = cont = 0

while True:
    n = int(input('Digite um número inteiro: [Para sair digite 999]: '))
    
    if n == 999:
        break

    cont += 1
    soma += n
    
print(f'Foram digitados {cont} números')
print(f'A soma dos números foi {soma}')
