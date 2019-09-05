# DESAFIO 004 - Leia entradas do teclado e mostre o seu tipo primitivo e todas as informações possíveis sobre ele

i = input('Digite alguma coisa, qualquer coisa: ')
print('O tipo primitivo de {}'.format(i),' é ',type(i))
print('E ele é numérico?', i.isnumeric())
print('Ele é alfabético?', i.isalpha())
print('Ele é alfanumérico?', i.isalnum())
print('Tem somente "espaço"? ', i.isspace())
print('Está tudo em maiúsculo? ', i.isupper())
print('Está tudo em minúsculo?', i.islower())
print('Está capitalizado? ', i.istitle())