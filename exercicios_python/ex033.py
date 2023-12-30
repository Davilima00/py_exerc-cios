a = int(input("Digite um primeiro número: \n"))
b = int(input("Digite um segundo número: \n"))
c = int(input("Digite um terceiro e último número: \n"))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O maior resultado foi: {}.".format(maior))
print("O menor resultado foi: {}.".format(menor))