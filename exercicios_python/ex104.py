# Verificar numero usando o isnumeric

def verif(texto):
    num = str(input(texto))
    t = num.isnumeric()

    while num.strip() == '':
        num = str(input('   Numero Invalido: '))
    while t == False:
        num = str(input('   Numero Invalido: '))
        t = num.isnumeric()
    return num


numero = verif('Digite um numero: ')
print(f"Vode digitou o numero {numero}")