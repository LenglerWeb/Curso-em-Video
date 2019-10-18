# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
# de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

print('Índice de Massa Corporal (IMC)')
altura = float(input('Por favor, informe a sual altura: (m) '))
peso = float(input('Agora, informe o seu peso: (Kg) '))

imc = peso / (altura * altura)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('\033[7;31;40mCUIDADO!\033[m , você está \033[4;33mAbaixo do Peso\033[m.')

elif imc >= 18.5 and imc < 25:
    print('\033[7;32;40mPARABÉNS!\033[m , você está no \033[4;33mPeso Ideal\033[m.')

elif imc >= 25 and imc < 30:
    print('\033[7;33;40mATENÇÃO!\033[m , você está com \033[4;33mSobrepeso\033[m.')

elif imc >= 30 and imc < 40:
    print('\033[7;31;40mATENÇÃO EM DOBRO!\033[m , você está com \033[4;33mObesidade\033[m.')

else:
    print('\033[7;31;40mURGENTE, PROCURE AJUDA!\033[m , você está com \033[4;33mObesidade Mórbida\033[m.')
