def calcular_media_ponderada():
    nota1 = float(input("Digite a Nota 1 (0-20): "))
    nota2 = float(input("Digite a Nota 2 (0-20): "))
    nota3 = float(input("Digite a Nota 3 (0-20): "))

    if (0 <= nota1 <= 20) and (0 <= nota2 <= 20) and (0 <= nota3 <= 20):
        media_final = (nota1 * 0.25) + (nota2 * 0.35) + (nota3 * 0.40)
        
        print(f"A média final ponderada é: {media_final:.2f}")

        if media_final > 9.5:
            print("O aluno está aprovado.")
        else:
            print("O aluno está reprovado.")
    else:
        print("As notas devem estar entre 0 e 20.")

calcular_media_ponderada()

