altura = float(input('Digite a sua altura em metros: '))
peso = float(input('Digite o seu peso em quilogramas: '))
imc = peso / (altura ** 2)

print('\nVeja a interpretação do IMC:')
print('''IMC      CLASSIFICAÇÃO      OBESIDADE (GRAU)
MENOR QUE 18,5        MAGREZA        0
ENTRE 18,5 E 24,9     NORMAL         0
ENTRE 25,0 E 29,9     SOBREPESO       I
ENTRE 30,0 E 39,9     OBESIDADE      II
MAIOR QUE 40,0        OBESIDADE GRAVE III''')

print(f'\nSeu IMC é: {imc:.1f}')

if imc < 18.5:
    print('Classificação: Magreza')
elif 18.5 <= imc <= 24.9:
    print('Classificação: Normal')
elif 25 <= imc <= 29.9:
    print('Classificação: Sobrepeso')
elif 30 <= imc <= 39.9:
    print('Classificação: Obesidade')
    print('Sua obesidade está no segundo grau. Procure ajuda.')
else:
    print('Classificação: Obesidade Grave')
    print('Sua obesidade está no terceiro grau. Procure ajuda.')

print('Tenha um bom dia!')
