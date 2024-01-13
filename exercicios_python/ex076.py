produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
            'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:.<30}R${produtos[i + 1]:>7.2f}')

print('-' * 40)

while True:
    produto = int(input('Digite o número do produto desejado (0 para encerrar): '))
    
    if produto == 0:
        print('Compra finalizada. Volte sempre!')
        break

    if 1 <= produto <= len(produtos) // 2:
        quantidade = int(input('Digite a quantidade desejada: '))
        valor_total = produtos[(produto - 1) * 2 + 1] * quantidade
        print(f'Você escolheu {quantidade} {produtos[(produto - 1) * 2]}(s) por R${produtos[(produto - 1) * 2 + 1]:.2f} cada.')
        print(f'Valor total: R${valor_total:.2f}')
    else:
        print('Produto inválido. Tente novamente.')

    print('-' * 40)
