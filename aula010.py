# Primeiro modelo de condiconal simples:
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Seu carro ainda é novo.')
else: 
    print('Seu carro não é mais novo!')

# Primeiro Exemplo:
print('=*' * 20)
print(" ")
nome = str(input('Informe o seu nome: '))
if nome == 'Gustavo':
    print('Seu nome é igual ao do professor!')
else:
    print('Seu nome NÃO É igual ao do professor ;)')
print('Bom dia {}!'.format(nome))

# Segundo Exemplo:
print('=*' * 20)
print(" ")
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2) / 2
if m >= 6:
    print('PARABÉNS, você está aprovado! Sua média é {}.'.format(m))
else:
    print('Sua média é {}, e você está REPROVADO!'.format(m))
