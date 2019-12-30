# Exercício Python 065: Crie um programa que leia vários números 
# inteiros pelo teclado. No final da execução, mostre a média 
# entre todos os valores e qual foi o maior e o menor valores 
# lidos. O programa deve perguntar ao usuário se ele quer ou 
# não continuar a digitar valores.

resposta = 'S'
cont = media = maior = menor = soma = 0 

while resposta in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n 
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
   
media = soma / cont    
print('A média foi {}'.format(media))
print('O maior número foi {}'.format(maior))
print('O menor número foi {}'.format(menor))
print('FIM')
