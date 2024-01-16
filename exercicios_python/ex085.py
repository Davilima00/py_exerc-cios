lista = list()
addp = list()
addi = list()

for c in range(7):
    n = int(input('digite um numero '))
    if n % 2 == 0:
        addp.insert(0, n)
    else:
        addi.insert(0, n)

lista.append(addp[:])
lista.append(addi[:])


print("os numeros pares sao", end=' ')
for d in lista[0]:
    print(d, end=' ')

print("\nos numeros impares sao", end=' ')
for e in lista[1]:
    print(e, end=' ')


    
