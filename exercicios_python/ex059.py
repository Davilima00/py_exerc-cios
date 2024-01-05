primeiro = int(input('primeiro valor: '))
segundo = int(input('segundo valor: '))


while True:
    print("""    [1] Somar 
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa""")
    opcao = int(input('>>>>>qual a sua opcao? '))
    if opcao == 1:
        soma = primeiro + segundo
        print(f"a soma entrer {primeiro}, {segundo} foi {soma}")
    elif opcao == 2:
        Multiplicar = primeiro * segundo
        print(f"a multiplicacao entre {primeiro}, {segundo} foi {Multiplicar}")
    elif opcao == 3:
        if primeiro == segundo:
            print("os dois possuem os mesmos valores")
        elif primeiro > segundo:
            print(f"O primeiro valor {primeiro} e maior")
        else:
            print(f"O segundo valor {segundo} e maior")
    elif opcao == 4:
        primeiro = int(input('primeiro valor: '))
        segundo = int(input('segundo valor: '))
    elif opcao == 5:
        break
    else:
        print("Voce nao digitou um numero valido")
print("tenha um bom dia")
