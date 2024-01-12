# Simulador de Caixa Eletrônico

print('=' * 30)
print('{:^30}'.format('BANCO DAVI'))
print('=' * 30)

# Solicita ao usuário o valor que deseja sacar
valor_saque = int(input('Que valor você quer sacar? R$ '))
total = valor_saque
cédulas = [50, 20, 10, 1]  # Lista com os valores das cédulas
total_cédulas = [0, 0, 0, 0]  # Lista para armazenar a quantidade de cédulas de cada valor

# Loop para contar as cédulas
for i in range(len(cédulas)):
    while total >= cédulas[i]: add ex0 
        total -= cédulas[i]
        total_cédulas[i] += 1

# Imprime o resultado
print('=' * 30)
print('Contagem de Cédulas:')
for i in range(len(cédulas)):
    if total_cédulas[i] > 0:
        print(f'{total_cédulas[i]} cédula(s) de R${cédulas[i]}')

print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')


