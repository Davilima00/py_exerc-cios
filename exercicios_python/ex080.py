lista = []

for _ in range(5):
    numero = int(input('Digite um número: '))

    if not lista or numero > lista[-1]:
        lista.append(numero)
        print(f'Adicionado ao final da lista.')
    else:
        for i in range(len(lista)):
            if numero <= lista[i]:
                lista.insert(i, numero)
                print(f'Adicionado na posição {i}.')
                break

print(f'Lista final ordenada: {lista}')
