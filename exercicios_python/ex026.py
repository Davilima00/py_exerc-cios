texto = str(input('digite ua frase')).strip().lower()
print('a letra a aparece {} vezes na frase'.format(texto.count('a')))
print('o primeiro a aparece na prosssicao {}'.format(texto.find('a')+1))
print('o primeiro a aparece na prosssicao {}'.format(texto.rfind('a')+1))