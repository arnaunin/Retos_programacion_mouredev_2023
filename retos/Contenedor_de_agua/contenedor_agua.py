from itertools import accumulate

# Función para buscar los maximos por la izquierda y por la derecha en cada posición
def buscar_maximos(array):
    
    max_izquierda = list(accumulate(array, max))
    max_derecha = list(accumulate(reversed(array), max))[::-1]

    return (max_izquierda, max_derecha)

# Funcion para calcular cuantas gotas quedaran atrapadas
def contenedor_agua(array):

    max_izquierda, max_derecha = buscar_maximos(array)
    
    gotas = sum(min(max_izquierda[i], max_derecha[i]) - array[i] for i in range(len(array)))

    return gotas

array = [4,5,2,1,5,7,8,1,2]

print(contenedor_agua(array))