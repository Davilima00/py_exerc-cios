dic = {}


dic['nome'] =  str(input('digite o nome do aluno '))
dic['media'] = float(input('digite a nota do aluno '))

if dic['media'] <= 7:
    print(f'aluno {dic["nome"]} foi reprovado')
else:
    print(f'O aluno {dic["nome"]} foi aprovado')

print(f'o nome e igual a {dic["nome"]}')
print(f'a media e igual a {dic["media"]}')

