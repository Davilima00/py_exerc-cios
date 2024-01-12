numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))

cont9 = 0
cont3 = 0
contpar = 0

print('Os números digitados foram:', end=' ')
for n in numeros:
    print(n, end=' ')

    if '9' in str(n):
        cont9 += 1
    if '3' in str(n):
        cont3 += 1

    if n % 2 == 0:
        # número par
        contpar += 1

print(f'\nQuantidade de números com o dígito 9: {cont9}')
print(f'Quantidade de números com o dígito 3: {cont3}')
print(f'Quantidade de números pares: {contpar}')
