# Exercício Python 071: Crie um programa que simule o funcionamento de um
# caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser
# sacado (número inteiro) e o programa vai informar quantas cédulas de cada
# valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("#" * 20)
print(" CAIXA 24 Horas ")
print("#" * 20)

totalNotas = 0
cedulas = 50

valor = int(input("Qual o valor do saque: R$"))
notas = valor

while True:

    if notas >= cedulas:
        notas -= cedulas
        totalNotas += 1
    else:
        if totalNotas > 0:
            print(f"Total de {totalNotas} cedulas de R${cedulas}")
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totalNotas = 0
        if notas == 0:
              break

print("Saque realizado com sucesso!",end='\n' "Volte sempre ;)")
