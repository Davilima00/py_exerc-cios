cont = 0
rodar = True
soma = 0

while rodar:
    numero = int(input('digite um numero [0 para parar] '))
    if numero == 0:
        rodar = False
    else:
        cont += 1
        soma += numero
        print(f"Voce digitou {cont} numeros e a soma deles foi {soma} ")
