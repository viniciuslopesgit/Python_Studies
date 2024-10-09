def converter_horario():
    hora = int(input("Digite a hora (0-23): "))
    minutos = int(input("Digite os minutos (0-59): "))

    if 0 <= hora <= 23 and 0 <= minutos <= 59:
        if hora == 0:
            hora_12 = 12
            periodo = "AM"
        elif hora == 12:
            hora_12 = 12
            periodo = "PM"
        elif hora > 12:
            hora_12 = hora - 12
            periodo = "PM"
        else:
            hora_12 = hora
            periodo = "AM"

        print(f"Resultado: {hora_12} {minutos:02d} {periodo}")
    else:
        print("Erro: Hora ou minutos inválidos.")

converter_horario()

