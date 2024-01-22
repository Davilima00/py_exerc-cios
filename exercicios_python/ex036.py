casa = int(input('digite o valor da casa '))
salario = int(input('digite o valor do seu salario '))
prestacao = int(input('quantos anos '))

valorpres = casa / prestacao
valorsala = (salario / (100/30))

print(f'para pagar uma casa de {casa} a prestaçao vai ser de {valorpres}')
if casa <= valorsala:
    print('seu emprestimo foi consebido')
else.:
    print('emprestimo negado')

