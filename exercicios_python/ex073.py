
from termcolor import colored

times_brasileirao = ('Flamengo', 'Palmeiras', 'Atlético-MG', 'Fortaleza', 'Bragantino', 'Fluminense', 'Bahia', 'Atlético-PR', 'Atlético-GO', 'Ceará', 'Corinthians', 'Santos', 'Internacional', 'Juventude', 'Sport', 'Cuiabá', 'São Paulo', 'América-MG', 'Grêmio', 'Chapecoense')

ordem = sorted(times_brasileirao)
time_procurado = 'Corinthians'

print(f'Cinco primeiros da tabela: {colored(times_brasileirao[:5], "green")}')
print(f'Últimos quatro times da tabela: {colored(times_brasileirao[-4:], "green")}')
print(f'Times do Brasileirão em ordem alfabética: {colored(ordem, "blue")}')
print(f'O Corinthians está na posição: {colored(times_brasileirao.index(time_procurado) + 1, "red")}')
