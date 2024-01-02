numero = int(input('Digite um número para ver a sua tabuada: '))

print(f'\nTabuada do {numero}:\n')

for c in range(0, 11):
    produto = c * numero
    print(f'{numero} x {c} = {produto}')

print('\nTenha um bom dia!')
