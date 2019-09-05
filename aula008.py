# Trabalhando com Módulos
# para importar existem 2 métodos;
# import bebidas -> importa todas as bebidas possíveis (ex.: refigerante, água, suco, chá, café, leite)
# import math
# from bebidas import café -> importa apenas um tipo de bebida (ex.: café)
# from math import sqrt

# Primeiro Método
import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
# print arredonda para cima
print('A raiz quadrada de {} é igual a {}'.format(num, math.ceil(raiz)))
# print arredonda para baixo
print('A raiz quadrada de {} é igiual a {}'.format(num, math.floor(raiz)))
# print padrão
print('A raiz quadrada de {} é igual a {:.2f}'.format(num, raiz))

# Segundo Método
from math import sqrt
num2 = int(input('Digite um outro numero: '))
raiz2 = sqrt(num2)
print('A Raiz Quadrada de {} é igual a {}'.format(num2, raiz2))

# Segundo Método com duas entradas
from math import sqrt, floor
num2 = int(input('Digite um outro numero: '))
raiz2 = sqrt(num2)
print('A Raiz Quadrada de {} é igual a {}'.format(num2, floor(raiz2)))