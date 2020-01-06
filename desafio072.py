# Exercício Python 072: Crie um programa que tenha uma dupla totalmente
# preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
# mostrá-lo por extenso.

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Trezes', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    numero = int(input("Digite um número entre 0 e 20: "))
    if 0 <= numero <= 20:
        print(f"Você digitou o número {extenso[numero]}")

        continuar = " "
        while continuar not in 'SN':
            continuar = str(input("Continuar? [S/N]")).strip().upper()[0]
        if continuar == 'N':
            print(">>> PROGRAMA ENCERRADO! <<<")
            break


