from random import choice
aluno1 = str(input('primeiro aluno: '))
aluno2 = str(input('primeiro aluno: '))
aluno3 = str(input('primeiro aluno: '))
aluno4 = str(input('primeiro aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
solteio = choice(lista)
print(f'O aluno escolido foi {solteio}')