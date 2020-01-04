# Variáveis Compostas -> TUPLAS
# OBS: AS TUPLAS IMUTÁVEIS

print("Variáveis Compostas -> TUPLAS")
print('OBS: AS TUPLAS IMUTÁVEIS!!!\n')

lanche = "Hamburger", "Suco", "Pizza", "Pudin", "Batata Frita"
print(f"A quantidade de itens na TUPLA é de {len(lanche)} elementos.\n")
print(f"A tupla lanche = {lanche}\n")
print(f"Mostrar o lanche[3]: {lanche[3]}\n")
print(f"Mostrar o lanche[0]: {lanche[0]}\n")
print(f"Mostrar o lanche[-2]: {lanche[-2]}\n")
print(f"Mostrar do lanche[1:3]: {lanche[1:3]}\n")
print(f"Mostrar do lancha[2:]: {lanche[2:]}\n")
print(f"Mostrar do lancha[:3]: {lanche[:3]}\n")
print(f"Mostrar o lanche[-2:]: {lanche[-2:]}\n")
print(f"Mostrar o lanche[-3:]: {lanche[-3:]}\n")

for c in lanche:
    print(f"Com o comando FOR para mostrar os itens dentro da TUPLA: {c}")

print("\nOutro modo de usar o comando FOR para listar os elementos dentro da TUPLA com o len(lanche):")
for c in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[c]}.")

print("\nMais um outro jeito de executar com o comando FOR:")
for pos, comida in enumerate(lanche):
    print(f"Vou comer {comida} que está na posição {pos} da TUPLA.")

print("\nPara listar os itens da TUPLA em ordem alfabética usar sorted(lanche).")
print(f"TUPLA ordenada: {sorted(lanche)}\n")

print("Concatenar duas TUPLAS em uma outra:")
a = (2, 4, 6)
b = (0, 1, 2, 6, 8, 9)
c = a + b
d = b + a
print(f"Concatenar as TUPLAS c = a + b: {c}")
print(f"Concatenar as TUPLAS d = b + a: {d}")
print(f"A quantidade de elementos da TUPLA c: {len(c)}")
print(f"Quantas vezes o número 6 está aparecendo na TUPLA c? {c.count(6)}")
print(f"Em qual posição está o número 8 na TUPLA c? Na posição {c.index(8)}")
print(f"Em qual posição está o número 9 na TUPLA d? Na posição {d.index(9)}")

pessoa = "Eduardo Lengler", 41, "Masculino", 79
print(f"\nInformações do: {pessoa}\n")

