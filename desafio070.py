# Exercício Python 070: Crie um programa que leia o nome e o preço de vários
# produtos. O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.


print("-" * 19)
print("LOJÃO SUPER BARATO")
print("-" * 19)

cont = total = menorpreco = maisquemil= 0
produto = ' '
while True:
    nome = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$"))

    cont += 1
    total += preco
    
    if preco >= 1000:
        maisquemil += 1
        
    if cont == 1 or preco < menorpreco:
        menorpreco = preco
        produto = nome
    
    continuar = " "
    while continuar not in 'SN':
        continuar = str(input("Continuar? [S/N]")).strip().upper()[0]
    if continuar == 'N':
        break

print(f"TOTAL: R${total:.2f}")
print(f"Houve {maisquemil} produto(s) acima de R$1000.00")
print(f"O produto mais barato foi {produto} que custa R${menorpreco:.2f}")
print("FIM")
