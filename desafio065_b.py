# Exercício Python 065: Crie um programa que leia vários números 
# inteiros pelo teclado. No final da execução, mostre a média 
# entre todos os valores e qual foi o maior e o menor valores 
# lidos. O programa deve perguntar ao usuário se ele quer ou 
# não continuar a digitar valores.

resposta = 'S'
media = maior = menor = cont = 0

#n = int(input('Digite um número inteiro: '))

while resposta == 'S':
    
    n = int(input('Digite um número inteiro: '))

    media += n
    cont +=1

    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    
    resposta = str(input('Desesa continuar? [S/N]: ')).strip().upper()[0]

media = media / cont
print('Foram digitados {} números.'.format(cont))
print('A MÉDIA foi {}'.format(media))
print('MAIOR valor digitado: {}'.format(maior))
print('MENOR valor digitado: {}'.format(menor))
print('FIM')    
