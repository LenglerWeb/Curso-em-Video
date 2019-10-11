#Condições Aninhadas

# if carro.esquerda():
#   bloco 1
# elif carro.direita():
#   bloco 2
# elifi carro.ré():
#   bloco 3
# else:
# bloco 4

nome = str(input('Qual o seu nome: ')).strip()
if nome == 'Gustavo':
    print('Seu nome é igual ao do professor!  ;)')
elif nome == 'Maria' or nome == 'Joao' or nome == 'Jose':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Olivia Daniele Nancy Amanda':
    print('Seu nome é igual ao das mulheres da minha família!')
else:
    print('Prazer em te conhecer!')
print('Tenha um bom dia, {}.'.format(nome))