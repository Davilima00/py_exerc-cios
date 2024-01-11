soma = 0
menor = 0
cont = 0 
cont1000 = 0

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    continuar = str(input('Quer continuar [S/N]: '))

    cont += 1
    soma += preco

    if preco > 1000:
        cont1000 += 1

    if cont == 1 or preco < menor:
        menor = preco

    if continuar.upper() == 'N':
        break

print(f"O total de compras foi {soma:.2f}")
print(f"Temos {cont1000} produtos custando mais de 1000")
print(f"O produto mais barato custa: {menor:.2f}")

        

         
