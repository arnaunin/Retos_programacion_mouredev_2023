def anios_bisiestos(anio):
    
    contador = 0

    while contador < 30:
        if anio % 4 == 0:
            print(anio)

            contador += 1

        anio += 1

    return

anios_bisiestos(2024)
    