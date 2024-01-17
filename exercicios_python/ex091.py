from random import randint
from operator import itemgetter
from time import sleep


dic = {'jogador_1': randint(1, 9),
       'jogador_2': randint(1, 9),
       'jogador_3': randint(1, 9),
       'jogador_4': randint(1, 9)}
       
print('-='*30)
for jogador, numero in dic.items():
    print(f"O {jogador} tirou {numero}")
    sleep(0.5)


print('-='*30)
rank = sorted(dic.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(rank, start=1):
    print(f'{i} lugar: {v[0]} com {v[1]:}')
    sleep(0.5)
print('-='*30)
