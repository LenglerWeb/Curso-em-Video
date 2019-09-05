# Operadores lógicos ( Aritméticos )
# Adição +
# Subtração -
# Multiplicação *
# Divisão /
# Potência **
# Divisão Inteira //
# Resto da Divisão %

############################
### ORDEM DE PRECEDÊNCIA ###

# 1. ()
# 2. **
# 3. * / // %
# 4. + -
############################

n1 = int(5)
n2 = int(2)
s = n1 + n2
print('Adição de {} + {} = {}'.format(n1, n2, s))
su = n1 - n2
print('Subtração de {} - {} = {}'.format(n1, n2, su))
m = n1 * n2
print('Multiplicação de {} * {} = {}'.format(n1, n2, m))
d = n1 / n2
print('Divisão de {} / {} = {}'.format(n1, n2, d))
p = (n1 ** n2)
print('Potenciação de {} ** {} = {}'.format(n1, n2, p))
di = n1 // n2
print('Divisão Inteira de {} // {} = {}'.format(n1, n2, di))
rd = n1 % n2
print('Resto da Divisão de {} % {} = {}'.format(n1, n2, rd))
