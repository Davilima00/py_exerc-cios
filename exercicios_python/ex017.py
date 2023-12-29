from math import hypot
comprimento_oposto = float(input('comprimento do cateto oposto '))
comprimento_adjacente = float(input('comprimento do cateto adjacente '))
hipotenusa = hypot(comprimento_oposto, comprimento_adjacente)
print(f"A hipotenusa vai medir {hipotenusa:.2f}")