def calc_album_duration():
    total_segundos = 0

    for i in range(1, 6): #loop para 5 canções
        print(f"\nCanção {i}:")
        minutos = int(input(f"Introduza os minutos da música {i}:"))
        segundos = int(input(f"Introduza os segundos da música {i}:"))
        
        #Converte a duração da canção para segundos e adiciona ao total
        total_segundos += minutos * 60 + segundos

    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60

    print(f"\nTotal do Álbum: {horas}h {minutos}m {segundos}s")

calc_album_duration()
