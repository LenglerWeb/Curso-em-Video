# Refaça o desafio035 dos triângulos, acescentando o recurso de mostrar 
# que tipo de triângulo será formado:
# - Equilátero: Todos os lados IGUAIS
# - Isósceles: Dois lados Iguais
# - Escaleno: Todos os lados DIFERENTES

a = int(input('Informe o primeiro segmento de reta: '))
b = int(input('Informe o segundo segmento de reta: '))
c = int(input('Informe o terceiro segmento de reta: '))

if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Os segmentos acima \033[7;33;40mPODEM FORMAR\033[m um trângulo ', end='')
    
    # if a == b == c:
    if a == b and b == c:
        print('\033[7;32;40mEQUILÁTERO!\033[m')
    # elif a != b != c !=a
    elif a != b and b != c and a != c:
        print('\033[7;32;40mESCALENO!\033[m')
    else:
        print('\033[7;32;40mISÓSCELES!\033[m') 
else:
    print('Infelizmente os segmentos acima \033[7;31;40mNÃO FORMAM\033[m um triângulo!')