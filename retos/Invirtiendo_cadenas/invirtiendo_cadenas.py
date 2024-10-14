def invertir(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida

    return cadena_invertida

print(invertir("Hola mundo"))