def fatorial(n, show=False):
    """
    Calcula o fatorial de um número.

    :param n: Número para calcular o fatorial.
    :param show: Se True, mostra o processo de cálculo.
    :return: O resultado do fatorial.
    """
    resultado = 1
    for i in range(n, 0, -1):
        resultado *= i
        if show:
            print(f'{i}', end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return resultado


# Exemplo de uso:
num = int(input('Digite um número para calcular o fatorial: '))
mostrar_processo = input('Deseja mostrar o processo? (S/N): ').upper() == 'S'

print(fatorial(num, show=mostrar_processo))


