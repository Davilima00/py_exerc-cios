dias = int(input('quantos dias alugados'))
km = float(input('quantos km rodados '))
valor = (dias * 60) + (km * 0.15)
print(f'o total a pagar e de {valor:.2f}')
