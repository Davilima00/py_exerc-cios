numero = int(input('digite um numero'))
print(f'analizando o numero {numero}')
uni = numero // 1 % 10
des = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10
print(f' a unidade desse numero é {uni}')
print(f' a dessena desse numero é {des}')
print(f' a centena desse numero é {cen}')
print(f' o milhar desse numero é {mil}')