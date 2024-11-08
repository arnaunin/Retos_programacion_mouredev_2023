from datetime import datetime

def cuantos_dias(fecha1, fecha2):
    # Comprobamos que las cadenas tienen el formato requerido
    try:
        datetime.strptime(fecha1, "%d/%m/%Y")
        datetime.strptime(fecha2, "%d/%m/%Y")

    except ValueError:
        print('ERROR: las cadenas introducidas no tienen un formato correcto')
        return

    # Convertimos los strings de las fechas a tipo timedate (fecha)
    fecha1 = datetime.strptime(fecha1, "%d/%m/%Y")
    fecha2 = datetime.strptime(fecha2, "%d/%m/%Y")
    
    intervalo = fecha1 - fecha2
    intervalo = abs(intervalo).days # Hacemos el valor absoluto de la diferencia entre fechas i lo convertimos a un objeto de tipo Int
    
    return intervalo

print(cuantos_dias("08/03/2003","08/11/2024"))