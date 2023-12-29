largura_parede = float(input('largura da parede: '))
altura_parede = float(input('altura da parede: '))
area = largura_parede * altura_parede
litros = area / 2
print(f'sua parede tem a dimensão de {largura_parede}x{altura_parede} e a sua area e de {area}m2.')
print(f'para pintar essa parede, voce presisara de {litros}L de tinta.')
