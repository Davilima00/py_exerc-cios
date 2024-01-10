cont = 0
soma = 0
rodar = True

while rodar:
    numero = int(input('Digite um número: '))
    continuar = input('Digite [N/S] para parar: ').strip().upper()
    
    soma += numero
    cont += 1
    
    if continuar == 'N':
        rodar = False

print(f"Você digitou {cont} vezes e a soma deles foi {soma}")
    
