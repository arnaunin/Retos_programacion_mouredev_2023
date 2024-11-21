# Funcion para dibujar cuadrados
def dibujar_cuadrado(lado):
    for i in range(lado):
        print(' * ' * lado)

# Funcion para dibujar tringulos rectangulos (punta arriba)
def dibujar_triangulo(lado):
    i = 1
    j = lado
    while i < (lado+1):
        # Espacios antes de los asteriscos
        print(' ' * j, end='')
        # Dibujamos los asteriscos del medio intercalados con espacios
        for x in range(1, i+1):
            # Si es el primer asterisco lo dibujamos solo, sin espacios
            if i == 1:
                print('*', end='')
            else:
                print('* ', end='')
        # Espacios despues de los asteriscos
        print(' ' * j)
        j -= 1
        i += 1

# Función para dibujar un triangulo invertido (función axuiliar para dibujar la parte inferior del rombo)
def dibujar_triangulo_invertido(lado):
    i = 2
    j = lado-1
    while i < (lado+1):
        # Espacios antes de los asteriscos
        print(' ' * i, end='')
        # Dibujamos los asteriscos del medio intercalados con espacios
        for x in range(1, j+1):
            # Si es el primer asterisco lo dibujamos solo, sin espacios
            if j == 1:
                print('*', end='')
            else:
                print('* ', end='')
        # Espacios despues de los asteriscos
        print(' ' * i)
        j -= 1
        i += 1

# Funcion para dibujar rombos
def dibujar_rombo(lado):
    # Dibujamos el triangulo superior
    dibujar_triangulo(lado)
    # Dibujamos el triangulo inferior
    dibujar_triangulo_invertido(lado)

# Función para dibujar hexagonos
def dibujar_hexagono(lado):
    # Dibujamos la parte superior
    for i in range(lado):
        # Espacios iniciales para centrar
        print(' ' * (lado - i - 1), end='')
        # Asteriscos intercalados con espacios
        print('* ' * (lado + i))
        
    # Dibujamos la parte inferior
    for i in range(lado - 2, -1, -1):
        # Espacios iniciales para centrar
        print(' ' * (lado - i - 1), end='')
        # Asteriscos intercalados con espacios
        print('* ' * (lado + i))


# Funcion para dibujar cualquier figura
def dibuja_figura(figura, lado):

    if figura not in ['cuadrado', 'triangulo', 'rombo', 'hexagono']:
        print("ERROR: Figura no válida. Por favor elige: cuadrado, triangulo o rombo.")
        return

    elif figura == 'cuadrado':
        dibujar_cuadrado(lado)
                    
    elif figura == 'triangulo':
        dibujar_triangulo(lado)

    elif figura == 'rombo':
        dibujar_rombo(lado)

    elif figura == 'hexagono':
        dibujar_hexagono(lado)

dibuja_figura('hexagono', 4)