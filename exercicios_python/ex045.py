from random import randint
from time import sleep

print('''suas opcoes
[1] pedra
[2] papel
[3] tesoura''')

jogador = int(input('qual e a sua jogada '))
pc = randint(1, 3)

sleep(0.75)
print('JO')
sleep(0.75)
print('KEN')
sleep(0.75)
print('PO')
sleep(0.75)

if pc == 1:
    print('pc escolheu pedra')
    if jogador == 1:
        print('vc escolheu pedra')
        print('empate')
    elif jogador == 2:
        print('vc escolheu papel')
        print('vc ganhou')
    elif jogador == 3:
        print(' vc escolheu tessoura')
        print('vc perdeu')
    else:
        print('vc não digitou um numero entre 1, 2 e 3')

elif pc == 2:
    print('pc escolheu papel')
    if jogador == 1:
        print('vc escolheu pedra')
        print('vc perdeu')
    elif jogador == 2:
        print('vc escolheu papel')
        print('empate')
    elif jogador == 3:
        print(' vc escolheu tessoura')
        print('vc ganhou')
    else:
        print('vc não digitou um numero entre 1, 2 e 3')

elif pc == 3:
    print('pc escolheu tesoura')
    if jogador == 1:
        print('vc escolheu pedra')
        print('vc ganhou')
    elif jogador == 2:
        print('vc perdeu')
        print('vc escolheu papel')
    elif jogador == 3:
        print(' vc escolheu tessoura')
        print('empate')
    else:
        print('vc não digitou um numero entre 1, 2 e 3')
        