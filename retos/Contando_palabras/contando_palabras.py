import string

texto = "hola mundo, hola mundo, hola mundo"
lista_texto = list(texto) # Convertimos la string en una lista

palabras = {}

while lista_texto: # Mientras esa lista tenga valores la seguimos recorriendo
    palabra = '' # Inicializamos la palabra

    while lista_texto and lista_texto[0].isalpha(): # Mientras la lista tenga valores i el primero sea una letra la iteramos
        letra = lista_texto[0].lower()
        palabra += letra # Añadimos la letra a la palabra
        lista_texto.pop(0) # Eliminamos el primer elemento de la lista para actuar sobre el siguiente en la siguiente iteracion

    # Eliminamos cualquier carácter no alfabético (como espacio o puntuación)
    if lista_texto:
        lista_texto.pop(0) # Esto elimina el carácter que no es alfabético

    # Añadimos la palabra al diccionario o incrementamos su contador
    if len(palabra) > 0:  # Solo actuamos si la palabra no está vacía
        if palabra in palabras:
            palabras[palabra] += 1  # Incrementamos el contador
        else:
            palabras[palabra] = 1  # Agregamos la nueva palabra con un contador inicial de 1


# Recuento final
for palabra, veces in palabras.items():
    print(f"{palabra}: {veces}")
