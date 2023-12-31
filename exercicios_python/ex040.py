nota1 = float(input('digite a primeira nota \n'))
nota2 = float(input('digite a primeira nota \n'))
soma = (nota1 + nota2) / 2
if soma >= 7:
    print('aluno aprovado')
elif soma >= 5 and soma <7:
    print('aluno de recuperacao')
elif soma < 5:
    print('aluno reprovado')
