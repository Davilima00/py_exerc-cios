dados_pessoas = []
pessoa = []
peso_max = peso_min = 0

while True:
    nome = str(input('Digite o nome da pessoa: '))
    peso = float(input('Digite o peso da pessoa: '))

    pessoa = [nome, peso]
    dados_pessoas.append(pessoa[:])

    if len(dados_pessoas) == 1:
        peso_max = peso_min = peso
    else:
        if peso > peso_max:
            peso_max = peso
        elif peso < peso_min:
            peso_min = peso

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(dados_pessoas)} pessoas.')
print(f'O maior peso foi de {peso_max:.2f}kg. Peso de ', end='')

for pessoa in dados_pessoas:
    if pessoa[1] == peso_max:
        print(f'[{pessoa[0]}] ', end='')

print(f'\nO menor peso foi de {peso_min:.2f}kg. Peso de ', end='')

for pessoa in dados_pessoas:
    if pessoa[1] == peso_min:
        print(f'[{pessoa[0]}] ', end='')
