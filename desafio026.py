#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a
# letra "A", em que posição ela aparece a primeira vez 
# e em que posição ela aparece a última vez.

letra = str(input('Digite uma frase qualquer: ')).strip().lower()
print('Quantas vezes aparece a letra "a": {} vezes na frase.'.format(letra.count('a')))
print('A primeira letra "a" apareceu na posição: {}'.format(letra.find('a')+1))
print('A última letra "a" apareceu na posição: {}'.format(letra.rfind('a')+1))