"""
Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time do Grêmio.

"""
print("=" * 19)
print(" Brasileirão 2019: ")
print("=" * 19)

clubes = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará SC', 'Cruzeiro', 'CSA', 'Chapeconense', 'Avaí')
print(f"-> Os 5 primeiros times: {clubes[0:5]}")
print("=" * 25)
print(f"-> Os últimos 4 colocados: {clubes[-4:]}")
print("=" * 25)
print(f"-> Times em ordem alfabética: {sorted(clubes)}")
print("=" * 25)
print(f"-> Em que posição está o time do Grêmio: {clubes.index('Grêmio')+1}º lugar.")
