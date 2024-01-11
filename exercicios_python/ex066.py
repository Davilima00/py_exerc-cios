cont = 0
soma = 0

while True:
    numero = int(input('digite um numero [999 para parar]'))

    if numero == 999:
        break

    cont += 1
    soma += numero

print(f"Voce digitou {cont} numeros")
print(f"A soma deles e {soma}")
    