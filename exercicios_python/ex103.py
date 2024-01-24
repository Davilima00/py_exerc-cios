# registo de jogador avançado 

def registo(nome, gol):
    """
    Esse programa vai verificar:
    Se o nome do jogador foi digitado 
    Se o numero de gols  foi digitado
    """
    if nome == '':
        nome = '<jogador desconhecido>'
        print(f'{nome} fez',end=' ')
    if not isinstance(gol, int) and gol == '':
        gol = 0
        print()
    return nome, gol


print('-'*50)
jogador = input('nome do jogador? ')
gols = input('gols: ')
lista = registo(jogador, gols)

