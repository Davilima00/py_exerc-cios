# inputar o ano de nacimento e informar se [deve votar], [voto opicional] ou [voto origatorio]


def votar(ano):
    from datetime import date
    idade = date.today().year - ano
    print('-'*50)
    if idade < 16:
        return(f"Com {idade} anos. Nao vota")
    elif idade >= 16 and idade < 18:
        return(f'Com {idade} anos. Voto opicional')
    else:
        return(f'Com {idade} anos. Voto obrigatorio')
    

alguma = int(input('Em que ano vc nasceu? '))
votar(alguma)