print('Loja do Davi')
dinheiro = float(input('Preço das compras: '))

print('''Formas de pagamento:
[1] À vista
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

pagamento = int(input('Escolha a opção de pagamento: '))

if pagamento == 1:
    desconto = dinheiro * 0.10
    total = dinheiro - desconto
    print(f'Pagando à vista, você ganha 10% de desconto. Sua conta fica por R${total:.2f}')
elif pagamento == 2:
    desconto = dinheiro * 0.05
    total = dinheiro - desconto
    print(f'Pagando à vista no cartão, você ganha 5% de desconto. Sua conta fica por R${total:.2f}')
elif pagamento == 3:
    print(f'OK, sua conta ficou por R${dinheiro:.2f}')
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = dinheiro * 1.20
    valor_parcela = juros / parcelas
    print(f'Parcelando em {parcelas} vezes, sua conta fica por R${juros:.2f}, com parcelas de R${valor_parcela:.2f}')
else:
    print('Você não digitou um número entre 1, 2, 3 e 4')

print('Tenha um bom dia!')
