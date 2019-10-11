# 037: Escreva um programa em Python que leia um número inteiro qualquer e peça 
# para o usuário escolher qual será a base de conversão: 
# 1 para binário, 
# 2 para octal e 
# 3 para hexadecimal.

n = int(input('Digite um número inteiro: '))
print('\033[1;32;41mEscolha uma base para conversão:\033[m')
print('[ 1 ] converter para \033[7;30;42mBINÁRIO\033[m')
print('[ 2 ] converter para \033[7;30;42mOCTAL\033[m')
print('[ 3 ] converter para \033[7;30;42mHEXADECIMAL\033[m')
n2 = int(input('Sua opção: '))

if n2 == 1:
   print('O número {}, convertido para BINÁRIO: {}'.format(n, bin(n)[2:]))

elif n2 == 2:
    print('O número {}, convertido para OCTAL: {}'.format(n, oct(n)[2:]))

elif n2 == 3:
    print('O número {}, convertido para HEXADECIMAL: {}'.format(n, hex(n)[2:]))

else:
    print('Opção INVÁLIDA!')