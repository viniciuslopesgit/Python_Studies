def calcular_imposto_salario():
    salario = float(input("Introduza um salário: "))

    imposto = 0

    if salario <= 15000:
        imposto = salario * 0.20
        taxa = 20
    elif salario <= 20000:
        imposto = 15000 * 0.20 + (salario - 15000) * 0.30
        taxa = 30
    elif salario <= 25000:
        imposto = 15000 * 0.20 + 5000 * 0.30 + (salario - 20000) * 0.35
        taxa = 35
    else:
        imposto = 15000 * 0.20 + 5000 * 0.30 + 5000 * 0.35 + (salario - 25000) * 0.40
        taxa = 40

    print(f"Paga taxa de {taxa}%: {imposto:.2f}€")

calcular_imposto_salario()

