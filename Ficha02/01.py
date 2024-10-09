def calc_maior():
    num1 = int(input("Introduza o primeiro valor: "))
    num2 = int(input("Introduza o segundo valor: "))

    if (num1 > num2):
        print(f"O maior número é: {num1}")
    elif (num1 < num2):
        print(f"O maior número é: {num2}")
    else:
        print("O números são iguais.")

calc_maior()
