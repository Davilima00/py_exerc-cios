def escrever(nome):
    print('-' * (len(nome) + 2))
    print(f"{nome:^{len(nome) + 2}}")
    print('-' * (len(nome) + 2))
    
def verificar(contar):
    while contar.lower() not in 'ns':
        contar = input('ERRO! Digite [N/S]: ')
    return contar.lower()


while True:
    entrada = str(input('Digite algo: '))
    escrever(entrada)
    cont = str(input('Continuar [N/S]: '))
    if verificar(cont) == 'n':
        break

    








