# registo de jogador

time = list()
jogador = dict()
gols = list()


while True:
    jogador = dict()
    gols = list()


    jogador['Nome'] = str(input('Nome do jogador '))

    jogos = int(input(f'Quantos partidas {jogador["Nome"]} jogou? '))
    for cgols in range(jogos):
        gols.append(int(input(f'gols na partida {cgols}: ')))

    jogador['gols'] = gols[:]
    jogador['Total'] = sum(gols)
    time.append(jogador)

    parar = str(input('quer continuar? [S/N]')).upper()
    while parar not in "SN":
        parar = str(input('ERRO!digite apenas [S/N]')).upper()
    if parar == 'N':
        break

print('-='*30)
print('Nome         gols        total')
print('-'*30)

for c, d in enumerate(time):
    print(f'  {c} {d["Nome"]}    {d["gols"]}         {d["Total"]}')

while True:
    mostrar = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if mostrar == 999:
        break

    if mostrar < len(time):
        print(f'-- Levantamento do jogador {time[mostrar]["Nome"]}:')
        for i, g in enumerate(time[mostrar]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    else:
        print('Jogador não encontrado!')
        for c, d in enumerate(time):
            print(f'  {c} {d["Nome"]}    {d["gols"]}         {d["Total"]}')

