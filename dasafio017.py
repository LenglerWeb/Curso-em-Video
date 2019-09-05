# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# Calcule e mostre o comprimento da hipotenusa

from math import hypot
catetoopo = int(input('Informe o Cateto Oposto: '))
catetoadj = int(input('Informe o Cateto Adjacente: '))
catopo = catetoopo ** 2
catadj = catetoadj ** 2

print('Valor do Cateto Oposto: {}'.format(catopo))
print('Valor do Cateto Adjacente: {}'.format(catadj))
print('O valor da Hipotenusa {}'.format(hypot(catetoopo, catetoadj)))
