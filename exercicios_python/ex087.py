m1 = [[], [], [], [], [], [], [], [], []]

for c in range(9):
    m1[c].append(int(input('digite u numero')))

print('-=' *30)
print(m1[0:3])
print(m1[3:6])
print(m1[6:])
print('-=' *30)

par = 0
for c in m1:
    for r in c:
        if r % 2 == 0:
            par += r

soma = 0
for tre in m1[6:]:
    for tri in tre:
        soma += tri

mai = 0
for co in m1[3:6]:
    for nu in co:
        if nu > mai:
            mai = nu

print(f'A soma dos valores pares e {par}')
print(f'A soma dos valores da treceira colua e {soma}')
print(f'O maior valor da segunda lina e {mai}')
print('-=' *30)

