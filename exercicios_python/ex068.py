from random import randint
from time import sleep

cont = 0

while True:
    print("Jogo do Davi ÍMPAR OU PAR")
    cont += 1

    escolha_jogador = input('Digite [I/P] para ÍMPAR ou PAR: ')
    numero_jogador = int(input('Digite um número: '))
    numero_pc = randint(1, 2)

    soma1 = (numero_jogador + numero_pc) % 2
    soma = (numero_jogador + numero_pc)

    sleep(1)

    if escolha_jogador.upper() == 'I':
        if soma1 != 0:
            print(f"Você jogou {numero_jogador} e o computador {numero_pc}. O total de {soma} deu ÍMPAR")
            print("PARABENS voce ganhou")
        else:
            print('Você perdeu!')
            break

    elif escolha_jogador.upper() == 'P':
        if soma1 == 0:
            print(f"Você jogou {numero_jogador} e o computador {numero_pc}. O total de {soma} deu PAR")
            print("PARABENS voce ganhou")
        else:
            print('Você perdeu!')
            break

print(f"Você jogou {cont} vezes")
