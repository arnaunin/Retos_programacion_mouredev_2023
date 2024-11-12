def tres_en_raya(matriz):
    # Contamos la proporcion de X y de O que hay en la matriz y comprobamos si es correcta
    x = sum(fila.count('X') for fila in matriz)
    o = sum(fila.count('O') for fila in matriz)
    
    if abs(x - o) > 1: # Si la diferencia de restar una con otra es más grande de uno significa que la proporcion no es correcta
        return 'Nulo!'

    # Comprobamos quien ha ganado, si ha habido un empate o si han ganado los dos
    ganan_x = False
    ganan_o = False

    # Comprobamos si han ganado las X
    if any(fila.count('X') == 3 for fila in matriz): # Comprobamos las filas
        ganan_x = True
    elif any(all(matriz[i][j] == 'X' for i in range(3))  for j in range(3)): # Comprobamos las columnas
        ganan_x = True
    # Comprobamos las dos diagonales
    elif all(matriz[i][i] == 'X' for i in range(3)):
        ganan_x = True
    elif all(matriz[i][j] == 'X' for i, j in zip(range(3), range(2, -1, -1))):
        ganan_x = True

    # Comprobamos si han ganado las O
    if any(fila.count('O') == 3 for fila in matriz): # Comprobamos las filas
        ganan_o = True
    elif any(all(matriz[i][j] == 'O' for i in range(3))  for j in range(3)): # Comprobamos las columnas
        ganan_o = True
    # Comprobamos las dos diagonales
    elif all(matriz[i][i] == 'O' for i in range(3)):
        ganan_o = True
    elif all(matriz[i][j] == 'O' for i, j in zip(range(3), range(2, -1, -1))):
        ganan_o = True
    
    # Evaluamos los resultado los retornamos
    if ganan_x and ganan_o:
        return 'Nulo!'
    elif ganan_x:
        return 'X'
    elif ganan_o:
        return 'O'
    else:
        return 'Empate'

matriz = [['O','X','X'],
          ['X','X','O'],
          ['X','O','O']]

print(tres_en_raya(matriz))