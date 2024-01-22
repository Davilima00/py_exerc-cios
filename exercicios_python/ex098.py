from time import sleep


def contagem(lst):
    print('--'*30)
    print(f"Contagem de {lst[0]} até {lst[1]} de {lst[2]} em {lst[2]}")
    for g in range(lst[0], lst[1], lst[2]):
        print(g, end=' ', flush=True)
        sleep(0.5)
    sleep(1)
    print('Fim!')
    print('--'*30)


primeiro = [0, 11, 1]
segundo = [10, 0, -2]
m(primeiro)
contagem(segundo)













