soma = 0

for num in range(0, 6):
    numero = int(input('digite um numero '))
    if numero % 2 == 0:
        soma += numero
        
print(f'a soma entre todos os pares foram {soma}')
