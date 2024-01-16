expressao = str(input('Digite a sua equacao '))

abre = expressao.count('(')
fecha = expressao.count(')')

if abre == fecha:
    print('sua expressao esta correta')
else:
    print('sua expressao esta errada')




