from random import randint

print("""Eu sou o seu computador...
Acabei de pensar em um número entre 0 e 10.
Você consegue adivinhar qual foi?""")

pc = randint(0,10)
pessoa = int(input('Qual é o seu palpite? \n'))
vezes = 1

while pessoa != pc:

    if pessoa < pc:
        print('Mais... tente mais uma vez. ')
    else:
        print('Menos... tente mais uma vez. ')

    pessoa = int(input('qual seu palpite agora \n'))
    vezes += 1


print(f"parabens vc acertou\nvc acertou em {vezes} tentativas")
