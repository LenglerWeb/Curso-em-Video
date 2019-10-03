print('#' * 24)
print('# Fatiamento de texto: #')
print('#' * 24)

# mostra a frase completa:
fila = 'Curso em Video Python'
print(fila)

# mostra a frase do item 9 até o item 13 -> (14 -1)
frase = fila[9:14]
print(frase)

# mostra a frase pulando de 2 em 2 letras ou itens mostrando o que estiver na posição 2
frase2 = fila[9:21:2]
print(frase2)

# mostra do item 0 até o item 4 -> (5 -1)
frase3 = fila[:5]
print(frase3)

# mostra do item que estiver na 15 posição até o final (não sabendo o final)
frase4 = fila[15:]
print(frase4)

# mostra as letras da posição 9 pulando de 3 em 3 e mostrando a 3 letra
frase5 = fila[9::3]
print(frase5, '\n')


print('#' * 21)
print('# Análise de texto: #')
print('#' * 21)

# mostra quantas letras tem na frase
frase6 = len(fila)
print('A frase tem', frase6, 'itens')

# Mostra quantos "o" tem na frase
frase7 = fila.count('o')
print('Existem {} "o" na frase "{}"'.format(frase7, fila))

# Mostra quantas vezes a letra "o" aparece da posição 0 até a 12 -> (13-1)
frase8 = fila.count('o', 0 , 13)
print('Mostre quantas letras "o" tem entre a posição 0 até 13: {}'.format(frase8))

# Mostra qual a posição que foi encontrada uma letra, caracter ou frase dentro de uma fila, lista ou frase
frase9 = fila.find('deo')
print('Mostra em qual posição (array) foi encontrada a palavra "deo" na frase: Posição {}'.format(frase9))
# obs.: No exemplo frase9 = fila.find('Android') ele irá retornar o valor -1
# isso significa que não foi encontrado na lista a palavra pesquisada
frase9b = fila.find('Android')
print('No fila.find("Android"), irá retornar o valor "{}", porque dentro da frase "{}", não existe a palavra "Android".'.format(frase9b, fila))

# mostra se é Verdadeiro ou Falso se na frase existe a palavra Curso: 
frase10 = 'Curso' in fila
print(frase10, '\n')

print('#' * 17)
print('# Transformação #')
print('#' * 17)

# Trocar uma palavra por outra
frase11 = fila.replace('Python', 'Android')
print(frase11)

# deixar a palavra ou frase um Maiúscula
frase12 = fila.upper()
print(frase12)

# deixar a palavra ou frase um Minúscula
frase13 = fila.lower()
print(frase13)

# deixar a palavra ou frase um a primeira letra Maiúscula e as outras Minúscula
frase12 = fila.capitalize()
print(frase12)

# deixar a palavra ou frase um Maiúscula
frase12 = fila.upper()
print(frase12)

# Remove todos os espaços do inicio e do final de uma frase
fila = '    Aprendendo Python 3      '
frase13 = fila.strip()
print(frase13)

# Remover os espaços da direita
fila = 'Aprenda Python     '
print(fila.rstrip())

# Remover os espaços da esquerda
fila = '       Aprenda Python'
print(fila.lstrip(), '\n')


print('#' * 11)
print( '# Divisão #' )
print('#' * 11)

# Cria uma lista, dividindo as palavras da frase [
fila = 'Curso em Vídeo Python'
frase14 = fila.split()
print(frase14)
print(frase14[1::2], '\n')

print('#' * 10)
print('# Junção #')
print('#' * 10)

# Subtituir os espaços por um "-"
frase15 = '-'.join(fila)
print(frase15)

print("""Mussum Ipsum, cacilds vidis litro abertis. Atirei o pau no gatis, per gatis num morreus.
Mé faiz elementum girarzis, nisi eros vermeio.
Diuretics paradis num copo é motivis de denguis.
Sapien in monti palavris qui num significa nadis i pareci latim.""")

print(fila.upper().count('O'))

# Mostra a letra "e" que está na palavra Vídeo e mostre a terceira letra
dividido = fila.split()
print(dividido[2])
print(dividido[2][3])
 










