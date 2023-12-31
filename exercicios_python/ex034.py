salario = int(input('digite o valor do seu salario '))
if salario >=1200:
    print(f'com o reajuste quem ganhava {salario} passa a ganhar {salario +(salario * (10/100))}')
else:
    print(f'com o reajuste quem ganhava {salario} passa a ganhar {salario +(salario * (15/100))}')