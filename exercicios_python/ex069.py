cont_18 = 0
cont_homem = 0
cont_mulher_20 = 0

while True:
    print('Cadastre uma pessoa')

    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip()
    parar = str(input('Quer continuar [S/N]: ')).strip()

    if idade > 18:
        cont_18 += 1

    if sexo.upper() == 'M':
        cont_homem += 1

    if sexo.upper() == 'F' and idade >= 20:
        cont_mulher_20 += 1

    if parar.upper() == 'N':
        break

print(f"Total de pessoas com mais de 18 anos: {cont_18}")
print(f"Ao todo temos {cont_homem} homens cadastrados")
print(f"E temos {cont_mulher_20} mulheres com mais de 20 anos")
