from random import shuffle
aluno1 = str(input('primeiro aluno: '))
aluno2 = str(input('primeiro aluno: '))
aluno3 = str(input('primeiro aluno: '))
aluno4 = str(input('primeiro aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print(f'A sequencia e {lista}')

