print('Gerador de PA')
primeiro = int(input('Primeiro termo da PA '))
razao = int(input('Qual a razao? '))
val = True 
vezes = 0
while val:
    calculo = primeiro + razao
    vezes += 1

    print(f'{primeiro} > ', end=' ')
    print(f'{calculo} > ', end=' ')
    primeiro = calculo


    if vezes == 10 :
        val = False



