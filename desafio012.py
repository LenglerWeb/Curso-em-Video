# leia o preço de um produto e mostre o seu novo preço com 5% de desconto:

preco = float(input('informe o preço do produto: R$ '))
desc = preco * (5 / 100)
precodesc = preco - desc
print('O valos do produto com 5% de desconto é R$ {:.2f}'.format(precodesc))