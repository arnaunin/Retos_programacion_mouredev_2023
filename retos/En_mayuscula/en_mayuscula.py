def en_mayuscula(string):
    # Nos quedamos solo con las letras de la cadena
    palabras = ''.join(letra for letra in string if letra.isalpha() or letra == ' ')
    # Creamos una lista con todas las palabras
    lista_palabras = palabras.split()
    # Recorremos la lista de palabras i las substituimos por las palabras con la primera letra mayuscula
    for palabra in lista_palabras:
        string = string.replace(palabra, palabra[0].upper() + palabra[1:])

    print(string)

en_mayuscula("hola mundo!")
