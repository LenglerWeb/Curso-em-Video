# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias
# pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

print("*=" * 11)
print("  CADASTRE UM PESSOA")
print("*=" * 11)

conth = contm = contidade = contmaioridade = contmenoridade = 0
while True:
    sexo = " "
    idade = int(input('Idade: '))
    if idade >= 18:
        contmaioridade += 1
        contmenoridade += 1
    simnao = " "
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
        if sexo == "M":
            conth += 1
        if sexo == "F":
            if idade < 20:
                contm += 1
                
    while simnao not in "SN":
        simnao = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]

    if simnao == 'N':
        break
    
print(f'Quantas pessoas MAIORES de 18 anos: {contmaioridade} pessoa(s).')
print(f"Quantos HOMENS foram cadastrados: {conth}. ")
print(f'Quantas mulheres tem menos de 20 anos: {contm}.')
