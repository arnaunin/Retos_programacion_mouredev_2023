def carrera_obstaculos(pista, acciones):
    # Diccionario con los valores correctos según la acción
    movimientos = {'_': 'run', '|': 'jump'}
    pista_inicial = pista  # Guardamos la pista inicial para comparación
    pista = list(pista)    # Convertimos a lista para modificarla

    for i, (tramo, accion) in enumerate(zip(pista, acciones)):
        if accion != movimientos[tramo]:  # Comprobamos si la acción es incorrecta
            if accion == 'run':
                pista[i] = '/'
            elif accion == 'jump':
                pista[i] = 'x'

    pista = ''.join(pista)  # Convertimos la lista a cadena

    print("Carrera inicial  :", pista_inicial)
    print("Carrera finalizada:", pista)
    
    return pista_inicial == pista  # Compara la pista inicial con la modificada


# Ejemplo de prueba
acciones = ["run", "run", "run", "jump", "run", "jump", "run", "run"]
pista = "___|_|__"

print("Resultado:", carrera_obstaculos(pista, acciones))
