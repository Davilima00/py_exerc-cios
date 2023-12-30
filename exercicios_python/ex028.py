from random import randint
print('-' * 26)
print('seja vem vindo ao meu jogo')
print('-' * 26)
print('tente escolher o nuero do pc (1, 5)')
jogada = int(input('coloque aqui a sua jogada '))
pc = randint(1,5)
if jogada == pc:
    print('parabens vc ganhou')
else:
    print(f'vc errou o numero escolhido do pc foi {pc}')
