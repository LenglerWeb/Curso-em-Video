# 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
n3 = float(input('Informe a terceira nota: '))

m = float(n1 + n2 + n3) / 3

if m >= 7.0:
    print('A sua média é {:.1f}'.format(m))
    print('O aluno está \033[7;32;40mAPROVADO!\033[m PARABÉNS.')
elif m >= 5.0 and m < 7.0:
    print('A sua média é {:.1f}'.format(m))
    print('O aluno está em \033[7;33;40mRECUPERAÇÃO!\033[m Estude um pouco mais.')
else:
    print('A sua média é {:.1f}'.format(m))
    print('O aluno está \033[7;31;40mREPROVADO!\033[m Solicite a rematrícula para a mesma série.')
