nome = str(input('digite teu nome ')).strip().lower()
print('muito prazer em te conhecer')
nome1 = nome.split()
print('seu primeiro nome e {}'.format(nome1[0]))
print('seu ultimo nome e {}'.format(nome1[len(nome1)-1]))