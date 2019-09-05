# Ordem de calculos
print(5 + 3 * 2)
print(3 * 5 + 4 ** 2)
print(3 * (5 + 4) ** 2)

# exemplos em aula
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, a multiplicação é {} e a divisão é {:.3f} .'.format(s, m, d))
print('Divisão inteira {} e a potência é {}'.format(di, e))
print('A soma é {}, multiplicação é {} e a divisão é {:.2f}'.format(s, m, d), end=' ')
print('Divisão Inteira é {} e a Potência é {}'.format(di, e))


