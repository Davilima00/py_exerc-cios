lista = []


while True:
    lista.append(int(input('digite um valor ')))
    con = str(input('Quer continuar? [N/S] ')).strip()

    if con in 'Nn':
        break


lista.sort(reverse=True)
print(f"os valores em ordem decresente sao {lista}")

if 5 in lista:
    print("O valor 5 está presenta na lista")
else:
    print('O valor 5 nao esta presente na lista')