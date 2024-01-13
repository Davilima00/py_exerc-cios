palavras_escola = ('professor', 'aluno', 'sala', 'quadro', 'livro', 'prova', 'aula', 'ensino', 'aprendizado', 'materiais', 'exercício', 'escola', 'educação', 'conhecimento', 'avaliação')

cont = 0

for p in palavras_escola:
    print(f"\nna paravra {p} temos", end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')

