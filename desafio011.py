# Leia a largaura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la.
# Sabendo que cada litro de tinta pinta uma área de 2m quadrados:

al = float(input('Qual a altura da parede: '))
la = float(input('Qual a largura da parede: '))
ar = al * la
print('Área da parede: {:.2f} m2'.format(ar))
qtinta = ar / 2
print('É necessário {:.2f} de litros de tinta para pintar {:.2f} m2.'.format(qtinta, ar))