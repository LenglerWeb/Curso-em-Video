# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e da tangente de ângulo

import math
# from math import radians, sin, cos, tan
# seno = sin(radians(angulo))
# cosseno = cos(radians(angulo))
# tangente = tan(radians(angulo))
angulo = float(input('Informe o ângulo desejado: '))
radiano = math.radians(angulo)
# Definindo as variáveis:
# seno = math.sin(math.radians(angulo))
# cosseno = math.cos(math.radians(angulo))
# tangente = math.tan(math.radians(angulo))
print('O SENO do ângulo {} é {:.2f}'.format(angulo, math.sin(radiano)))
print('O COSSENO do ângulo {} é {:.2f}'.format(angulo, math.cos(radiano)))
print('A TANGENTE do ângulo {} é {:.2f}'.format(angulo, math.tan(radiano)))
