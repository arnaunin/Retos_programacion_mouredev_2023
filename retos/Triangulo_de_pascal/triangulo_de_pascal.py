# Función auxiliar para dibujar el triangulo
def dibujar_triangulo(triangulo):
    max_width = len(" ".join(map(str, triangulo[-1])))  # Ancho de la última fila
    # Recorremos todas la filas y las vamos imprimiendo en el centro
    for fila in triangulo:
        fila_str = " ".join(map(str, fila))
        print(fila_str.center(max_width))

# Función que calcula el triangulo dado el tamaño de los lados
def triangulo_de_pascal(lado):

    triangulo = []
    # Hacemos un bucle de un numero de iteraciones igual a las filas que tiene que tener el triangulo
    # Numero de filas = Tamaño del lado
    for fila in range(lado):
        
        numeros = []
        for valor in range(fila+1):

            # Casos para los primeros y los ultimos numeros de cada fila que siempre seran 1
            if valor == 0 or valor == fila:
                numero = 1
            # Casos para los numeros del medio
            else:
                numero = triangulo[fila-1][valor-1] + triangulo[fila-1][valor]
            
            numeros.append(numero)

        triangulo.append(numeros)
                
    dibujar_triangulo(triangulo)
        
triangulo_de_pascal(12)