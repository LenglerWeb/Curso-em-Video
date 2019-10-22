# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

p = str(input('Digite uma frase qualquer: ')).strip().upper()

cont = len(p)
print('Quantas letras tem a frase digitada: {}'.format(cont))

for c in range(cont, 0, -1):
   # print('{}'.format(p[0:c]))
    p2 = p[c-1]
    print(p2)  
    print('{}'.format(p[c-1]), end=' ')
print('')    #print('{}'.format(p[cont:0:-1]))