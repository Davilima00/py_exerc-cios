final = []

while True:
    dados = {}
    dados['Nome'] = str(input('O nome: '))
    sexo = str(input('O sexo [M/F]: '))

    while sexo not in 'MmFf':
        sexo = str(input('ERRO! Digite [M/F]: '))
    dados['Sexo'] = sexo

    dados['Idade'] = int(input('Digite a idade: '))
    parar = str(input('Quer continuar? [N/S]: '))

    while parar not in 'NnSs':
        parar = str(input('ERRO! Digite [N/S]: '))

    final.append(dados)
    if parar in 'Nn':
        break


print('-='*30)
print(f'Ao todo foram cadastradas {len(final)} pessoas')

media = sum(pessoa['Idade'] for pessoa in final) / len(final)
print(f'A média de idade é {media:.2f}')

print('As mulheres foram:', end=' ')
for pessoa in final:
    if pessoa["Sexo"].upper() == 'F':
        print(f'-> {pessoa["Nome"]}',end=' ')

# a listas de pessoas que estão acima da media

print('\nLista de pessoas que estao  acima da media')
print('')
for pessoa in final:
    if pessoa['Idade'] > media:
        print(f'      nome = {pessoa["Nome"]}; sexo = {pessoa["Sexo"]}; idade = {pessoa["Idade"]}.')
