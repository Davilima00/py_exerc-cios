from random import randint
from time import sleep

def gerar():
    num = []
    print('-'*60)
    for _ in range(5):
        num.append(randint(0, 9))
    print("soteando 5 valores da lista:", end=' ')
    for n in num:
        print(n, end=' ')
    print('PRONTO !')
    return num

def somar(lst):
    pares = [num for num in lst if num % 2 == 0]
    soma = sum(pares)
    print(f"A soma dos numeros {lst} foram {soma}")


for _ in range(90):
    sleep(1)
    numeros = gerar()
    final = somar(numeros)



