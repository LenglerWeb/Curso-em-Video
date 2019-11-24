cont = maior = menor = total = n = 0
while True:
    n = int(input('Digite um número inteiro [sair 999]: '))
    if n == 999:
        break
    cont += 1
    total += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(f'Maior = {maior}')
print(f'Menor = {menor}')
print(f'Soma total = {total}')
print('FIM')


