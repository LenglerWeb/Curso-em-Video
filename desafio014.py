# Faça um programa que converta a temperatura em graus Celsius para Fahrenheit

c = float(input('Informe a temperatura em Graus Celsius para converter em Fahrenheit. °C: '))
f = (c * 9/5) + 32
print('Conversão de {}°C para Fahrenheit: {}°F'.format(c, f))