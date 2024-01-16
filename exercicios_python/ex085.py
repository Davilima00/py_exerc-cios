lista = [[], []]

for c in range(7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

# Ordena as sublistas
lista[0].sort()
lista[1].sort()

print(f'Os números pares são {lista[0]}')
print(f'Os números ímpares são {lista[1]}')
