def calc_pontos():
    lugar = int(input("Digite a posição em que o piloto terminou a corrida: "))

    pontos_posicao = {
        1: 10,
        2: 8,
        3: 6,
        4: 5,
        5: 4,
        6: 3,
        7: 2,
        8: 1
    }

    if lugar in pontos_posicao:
        pontos = pontos_posicao[lugar]
        print(f"O piloto ganhou {pontos} pontos.")
    else:
        print(f"Posição inválida. Deve estar entre 1 e 8. ")

calc_pontos()
