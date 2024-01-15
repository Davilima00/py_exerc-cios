lista = []

while True:
    numero = int(input('Digite um número para colocar na lista: '))
    
    if numero not in lista:
        lista.append(numero)
        print("Número adicionado com sucesso.")
    else:
        print(f"O número {numero} já está na lista. Nao vou adicionar")

    cont = input('Quer continuar? [S/N] ').strip().upper()
    if cont == 'N':
        break

print(f'Lista final: {sorted(lista)}')

