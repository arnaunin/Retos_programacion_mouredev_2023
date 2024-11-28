import numpy as np

def numeros_perdidos(numeros):

    # Comprobamos que el array de entrada sea correcto
    if numeros.dtype != np.int64 or np.any(numeros != np.sort(numeros)) or len(numeros) != len(np.unique(numeros)):
        return "ERROR: El array de entrada no es correcto"
    
    mayor = max(numeros)
    menor = min(numeros)
    numeros_perdidos = [numero for numero in range(menor, mayor) if numero not in numeros]

    return numeros_perdidos

numeros = np.array([1,2,4,5,7,9,11], int)
print(numeros_perdidos(numeros))
