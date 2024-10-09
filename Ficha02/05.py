def menor_maior():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if num1 < num2:
        menor = num1
        maior = num2
    else:
        menor = num2
        maior = num1

    print(f"O menor número é: {menor}")
    print(f"O maior número é: {maior}")

menor_maior()

