soma = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i

print(f'A soma de todos os valores ímpares divisíveis por 3 no intervalo de 1 a 500 é {soma}')
