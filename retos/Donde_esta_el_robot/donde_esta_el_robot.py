# Función que calcula la dirección que tomará el robot
def mover_direccion(direccion):
    
    # Retorna la direccion en que va a estar el robot en el siguiente movimiento
    if direccion == (0,1):
        return (-1,0)
    
    elif direccion == (-1,0):
        return (0,-1)
    
    elif direccion == (0,-1):
        return (1,0)
    
    elif direccion == (1,0):
        return (0,1)


# Función que calcula la posición del robot después de varias secuencias de pasos
def calcular_posicion(array):
    
    # Posición en la que empieza el robot
    pos_actual = (0,0)

    # Direccion inicial en que empieza el robot
    direccion = (0,1)

    #  Recorremos el array de valor por valor
    for pasos in array:

        # Calculamos el movimiento que debe de hacer el robot multiplicando la direccion por los pasos
        movimiento = (pasos * direccion[0], pasos * direccion[1])

        if pasos < 0:
            movimiento = (-movimiento[0], -movimiento[1]) # Invertimos la direccion del movimiento en caso de que los pasos sean negativos

        # Calculamos en que posición quedará el robot sumando el movimiento a la posicion actual
        pos_actual = (pos_actual[0] + movimiento[0], pos_actual[1] + movimiento[1])

        # Calculamos con la función auxiliar cual será la siguiente dirección del robot
        direccion = mover_direccion(direccion)
        
    return pos_actual

print(calcular_posicion([10, 5, -2]))