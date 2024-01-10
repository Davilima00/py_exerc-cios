print('Gerador de [PA]')

termo1 = int(input('Primeiro termo: '))
razao = int(input('Razao da PA'))
numero = 1
vezes = 10

while numero <= vezes:
    print(f"{termo1} -> ", end=' ')
    termo1 += razao
    numero += 1

    if numero == vezes:
        continuar = int(input('\nQuantos termos vc quer mostrar a mais? '))
        # se continuar for igual a 0 parar o codigo
        vezes += continuar

print('fim')
