from random import randint


def linha(): # criando uma linha
    print('-'*60)

def maior(lst): # maior valor da lista
    mai = 0
    cont = 0
    linha()
    print('Analizando valores passados... ')
    for  num in lst:
        cont += 1
        print(num, end=' ')
        if cont == 1:
            mai = num
        if mai < num:
            mai = num
    print(f"foram informados {len(lst)} numeros ao total")
    print(f"o maior valor informado foi {mai}")

def gerar(): # gerar numeros na lista
    numeros = list()
    vezes = randint(0, 9)
    for num in range(vezes):
        numeros.append(randint(1, 10))
    return numeros


for c in range(4):
    numeros = gerar()
    maior(numeros)



