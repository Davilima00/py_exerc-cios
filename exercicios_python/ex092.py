dic = {'nome': str(input('Nome: ')),
'nacimento': (2024 - int(input('Ano de Nacimento: ')))}
cart = int(input('carteira de trabalho (0 não tem): '))

if cart == 0:
    print('-='*30)
    dic['ctps'] = cart
    for pri, segu in dic.items():
        print(f" - {pri} tem valor {segu}")
else:
    cont = int(input('Ano de contratação: '))
    sala = int(input('Salario: '))
    dic['ctps'] = cart
    dic['salario'] = sala
    dic['aposentadoria'] = dic['nacimento'] + 35
    for pri, segu in dic.items():
        print(f" - {pri} tem valor {segu}")
                                                                