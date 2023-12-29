from math import radians, sin, cos, tan
angulo = float(input('digite o angulo que vc deseja:'))
rad = radians(angulo)
print(f'o angulo de {angulo} tem o SENO de {sin(rad):.2f}')
print(f'o angulo de {angulo} tem o COSSENO de {cos(rad):.2f}')
print(f'o angulo de {angulo} tem o TANGENTE de {tan(rad):.2f}')
