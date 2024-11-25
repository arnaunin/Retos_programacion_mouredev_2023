def marco_de_palabras(texto):
    palabra_larga = len(max(texto.split(), key=len))

    # Imprimimos el borde superior
    print('*' * palabra_larga + 4 * '*')

    for palabra in texto.split():
        espacios = palabra_larga - len(palabra)
        print('* ' + palabra + ' ' * espacios + ' *')

    # Imprimimos el borde inferior
    print('*' * palabra_larga + 4 * '*')

marco_de_palabras("¿Qué te parece el reto?")