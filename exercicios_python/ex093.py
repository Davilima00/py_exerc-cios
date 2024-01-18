dados = {'nome': str(input('Nome do jogador '))}
gols = []
cont = 0


partidas = int(input(f'Quantas partidas {dados["nome"]} jogou '))
for jogos in range(partidas):
    numero = int(input(F'Gols da partida {jogos +1}: '))
    gols.append(numero)
    cont += numero

dados['gols'] = gols
dados['total'] = cont

print('-='*30)
print(dados)
print('-='*30)

for pri, seg in dados.items():
    print(f"o campo {pri} tem valor {seg}")
print('-='*30)

for partida in range(partidas):
    print(f'Na partida {partida + 1}, {dados["nome"]} fez {dados["gols"][partida]} gols.')

print(f'foi um total de {dados["total"]} gols')

