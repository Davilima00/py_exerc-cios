lista = []
par = []
impar = []


while True:
    numero = (int(input('digite um numero: ')))
    lista.append(numero)

    if numero % 2 == 0:
        par.append(numero)

    else:
        impar.append(numero)

    cont = str(input('Quer continuar? [N/S]'))

    if cont in "Nn":
        break

print(f"a sua lista inteira foi {lista}")
print(f"os numeros impares da sua lista sao {impar}")
print(f"os numeros pares da sua lista sao {par}")

