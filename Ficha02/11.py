def verificar_saldo():
    saldo = float(input("Digite o saldo da conta bancária: "))
    
    montante = float(input("Digite o montante a creditar (positivo) ou debitar (negativo): "))

    saldo_final = saldo + montante

    if saldo_final > 0:
        print(f"A operação é válida. O saldo final é: {saldo_final:.2f} €")
    else:
        print(f"A operação é inválida. O saldo final é: {saldo_final:.2f} €, o que não é permitido.")

verificar_saldo()

