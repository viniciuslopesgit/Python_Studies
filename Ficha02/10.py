def calculadora():
    num1 = float(input("Digite o primeiro número real: "))
    num2 = float(input("Digite o segundo número real: "))

    operacao = input("Digite a operação desejada (+, -, *, /): ")

    if operacao == '+':
        resultado = num1 + num2
        print(f"O resultado de {num1} + {num2} = {resultado}")
    elif operacao == '-':
        resultado = num1 - num2
        print(f"O resultado de {num1} - {num2} = {resultado}")
    elif operacao == '*':
        resultado = num1 * num2
        print(f"O resultado de {num1} * {num2} = {resultado}")
    elif operacao == '/':
        if num2 != 0:  # Verifica se o denominador não é zero
            resultado = num1 / num2
            print(f"O resultado de {num1} / {num2} = {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Erro: Operação inválida. Por favor, use +, -, * ou /.")

calculadora()

