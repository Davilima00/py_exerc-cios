while True:
    numero = int(input('digite um numero para ver a sua tabuada '))
    if numero <= 0:
        break
        
    for cont in range(1,11):
        print(f"{cont} x {numero} = {cont * numero}")
