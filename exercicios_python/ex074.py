from random import randint

numeros = (randint(1, 99), randint(1, 99), randint(1, 99), randint(1,99), randint(1, 99))
print(f"solteiros de numeros ",end=' ')
for n in numeros:
    print(n, end=' ')
print(f'\no maior numero foi {max(numeros)}')
print(f'o menor numero foi {min(numeros)}')

