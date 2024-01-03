numero = int(input('Digite um número para saber se ele é primo: '))
divisores = 0

for cont in range(1, numero + 1):
    if numero % cont == 0:
        divisores += 1

if divisores == 2:
    print(f'O número {numero} é primo.')
else:
    print(f'O número {numero} não é primo.')