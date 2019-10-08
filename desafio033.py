# 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
ma = n1
me = n1

if n2 > n1 and n2 > n3:
    ma = n2
if n3 > n1 and n3 > n2:
    ma = n3
'''
if n1 > n2 and n1 > n3:
    ma = n1
if n1 < n2 and n2 > n3:
    ma = n2
if n1 < n2 and n2 < n3:
    ma = n3'''
print('O MAIOR número digitado foi: {}'.format(ma))
'''
if n1 < n2 and n1 < n3:
    me = n1
if n1 > n2 and n2 < n3:
    me = n2
if n1 > n2 and n2 > n3:
    me = n3'''

if n2 < n1 and n2 < n3:
    me = n2
if n3 < n1 and n3 < n2:
    me = n3
print('O MENOR número digitado foi: {}'.format(me))