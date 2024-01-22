def lin():
    print('-'*30)

def calc(a , l):
    calculo = a * l
    print(f"A area do terreno e {calculo}")


lin()
print("     Calculo de area")

al = float(input('Digite a altura '))
lar = float(input('Digite a largura '))
calc(al, lar)