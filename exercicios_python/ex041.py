from datetime import date 
atual = date.today().year
nacimento = int(input('ano de nacimento \n'))
idade = atual - nacimento
if idade <= 9:
    print('mirin')
elif idade > 9 and idade <= 14:
    print('infantil')
elif idade > 14 and idade <= 19:
    print('junior')
elif idade > 19 and idade <= 25:
    print('senior')
else:
    print('master')
