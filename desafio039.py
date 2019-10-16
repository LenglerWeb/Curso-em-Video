# 039: Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

print('Informe uma opção:')
print('[ 1 ] - Masculino')
print('[ 2 ] - Feminino')

sexo = int(input('Qual sua opção: '))
if sexo == 1:
    ano = int(input('Informe ano de nascimento: '))
    anoatual = 2019
# atual = date.today().year  (Usado pelo professor!)
    idade = anoatual - ano

    print('Quem nasceu em {} tem/terá {} anos em {}.'.format(ano, idade, anoatual))

    if idade < 18:
        falta = 18 - idade
        print('Ainda faltam {} anos para o alistamento.'.format(falta))
        print('Seu alistamento será em {}.'.format(anoatual + falta))
    
    elif idade == 18:
        print('Prepare-se para realizar o alistamento!')
    
    elif idade > 18:
        passou = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(passou))
        print('Seu alistamento foi em {}.'.format(anoatual - passou))

else:
    print('\033[7;32;40mMulheres não precisam se alistar, obrigado pela consulta!\033[m ')