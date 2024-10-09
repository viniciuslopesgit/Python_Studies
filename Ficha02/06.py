def maior_menor():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if num1 > num2:
        maior = num1
        menor = num2
    else:
        maior = num2
        menor = num1

    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")

maior_menor()

