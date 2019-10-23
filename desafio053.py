# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

palavra = str(input('Digite uma frase qualquer: ')).strip().upper()
palavra2 = palavra.split()
junto = ''.join(palavra2)
cont = len(junto)
inverso = ''

print('-' * 25)
print('Você digitou: {}'.format(palavra))
# print('Lista de Palavras: {}'.format(palavra2))
# print('Palavras todas junto: {}'.format(junto))
# print('Quantas letras tem a frase digitada: {}'.format(cont))
print('-' * 25)

for c in range(cont - 1, -1, -1):
    inverso += junto[c]

print('{} -> {}'.format(junto, inverso))

if junto == inverso:
    print('A Frase/Palavra \033[1;32mFORMA\033[m um PALINDROMO')
else:
   print('A Frase/Palavra \033[1;31mNÃO FORMA\033[m um PALINDROMO')
