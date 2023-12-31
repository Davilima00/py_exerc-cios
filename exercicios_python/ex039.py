from datetime import date 
atual = date.today().year
nasc = int(input('ano de nacimento \n'))
idade = atual - nasc
print(f'quem naceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('vc deve se aliatar esse ano')
elif idade < 18:
    saldo = 18 - idade
    print(f'ainda faltam {saldo} anos para seu alistamento ')
elif idade > 18:
    saldo = (18 - idade) * (-1)
    print(f' vc deveria ter se alistado ha {saldo} anos')
