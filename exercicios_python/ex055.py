maior_peso = 0
menor_peso = 0

for p in range(1, 6):
    peso = float(input(f"peso da {p} pessoa "))
    if p == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print(f"o maior peso lido foi de {maior_peso}")
print(f"o menor peso lido foi de {menor_peso}")