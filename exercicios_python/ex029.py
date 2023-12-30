velociadade = int(input('qual a velociade atual do carro '))
if velociadade > 80:
    print('multado vc execeo o limete')
    multa = velociadade - 80
    print(f'vc deve pagar uma multa de {multa * 7}')
else:
    print('tenha um bom dia ')
    print('dirija com seguranca')

