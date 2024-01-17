from random import randint
from operator import itemgetter

dic = {'jogador_1': randint(1, 9),
       'jogador_2': randint(1, 9),
       'jogador_3': randint(1, 9),
       'jogador_4': randint(1, 9)}

for jogador, numero in dic.items():
    print(f"O {jogador} tirou {numero}")

rank = sorted(dic.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(rank, start=1):
    print(f'{i} lugar: {v[0]} com {v[1]}.')
