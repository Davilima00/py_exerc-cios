numero = [int(input(f'digite o numerode prossição 0: ')), int(input(f'digite o numerode prossição 1: ')), int(input(f'digite o numerode prossição 2: ')), int(input(f'digite o numerode prossição 3: ')), int(input(f'digite o numerode prossição 4: '))]


maxx = max(numero)
prosmax = []

for nmax, pmax in enumerate(numero):
    if pmax == maxx:
        prosmax.append(nmax)

print(f"o maior numero e {maxx} e a prossicao dele e {prosmax}")

minn = min(numero)
prosmin = []

for nmin, pmin in enumerate(numero):
    if  pmin == minn:
        prosmin.append(nmin)

print(f"o menor numero e {minn} e a prossicao dele e {prosmin}")






