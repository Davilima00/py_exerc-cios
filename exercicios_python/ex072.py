
nomes = ('zero', 'um', 'dois', 'tres', 'quarto', 'cinco', 'seis', 'sete', 'oito', 'nove', 'des', 'onze', 'dose', 'trese', 'quartoze', 'quinze', 'deseseis', 'desesete', 'desoito', 'desenove', 'vinte')

while True:
    numero = int(input('digite um numero entre 0 e 20 '))
    if 0 <= numero <= 20:
        break
    else:
        print('Você não digitou um número entre 0 e 20.')


print(f'O número {numero} por extenso é: {nomes[numero]}')
