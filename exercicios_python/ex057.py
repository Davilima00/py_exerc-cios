n = str(input('informe teu sexo [M, F]')).strip().upper()

while n not in ['M', 'F']:
    n = str(input('dados invalidos. por favor, informe teu sexo [M, F]')).strip().upper()

if n == "F":
    print(f"Sexo feminino registrado com sucesso")
else:
    print("Sexo masculindo registrado com sucesso")
