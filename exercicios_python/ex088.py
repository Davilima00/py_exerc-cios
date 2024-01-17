from random import randint


print('-='*30)
print(f"{'Jogo da mega cena':^60}")
print('-='*30)

principal = []
segundo = []
tre = []
cont = 0
cont1 = 0


rodar = int(input('quanos jogos vc quer que eu sorteie? '))

while True:
    if cont <= rodar:
        while cont1 <= (6 * rodar):
            num = randint(0, 60)
            if num not in segundo and num not in principal:
                segundo.append(num)
                cont1 += 1
                cont += 1 
                if cont == 6:
                    principal.append(segundo[:])
                    segundo.clear()
                    cont = 0

            
    break
for c in principal:
    print(c)