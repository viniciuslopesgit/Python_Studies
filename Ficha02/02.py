def calc_imposto():
    salario = float(input("Introduza um salário: "))

    if (salario <= 15000):
        taxa = 0.20
    else:
        taxa = 0.30

    imposto = salario * taxa
    print(f"Resultado: {imposto:.2f}")

calc_imposto()
