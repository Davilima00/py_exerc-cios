lista = []
cadrasto = []
cont = 0

while True:
    cont += 1 
    nome = str(input(f'digite o nome do {cont}o. aluno '))
    nota1 = float(input('primeira nota '))
    nota2 = float(input('segunda nota '))
    parar = str(input('quer continuar? [N/S]'))

    cadrasto.append(nome)
    soma = (nota1 + nota2) / 2
    cadrasto.append(soma)
    cadrasto.append(nota1)
    cadrasto.append(nota2)
    lista.append(cadrasto[:])
    cadrasto.clear()

    if parar in 'Nn':
        break

print('-='*30)
co = 0
print('NO.  NOME.   MEDIA')
for c in lista:
    co += 1 

    print(f"{co}    {c[0]}      {c[1]}")
print('-='*30)

while True:
    mostrar = int(input('Mostrar notas de qual aluno? (0 interrompe) '))
    if mostrar == 0:
        break
    if 1 <= mostrar <= len(lista):
        print(f'As notas de {lista[mostrar-1][0]} são: {lista[mostrar-1][2]} e {lista[mostrar-1][3]}')
    else:
        print('Aluno não encontrado. Tente novamente.')