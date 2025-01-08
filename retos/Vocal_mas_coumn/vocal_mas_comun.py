import unicodedata

# Función que normaliza las vocales del texto y las deja en su forma base
def normalizar_texto(texto):
    # Descomponer caracteres unicode en base + diacríticos
    texto_normalizado = unicodedata.normalize('NFD', texto)
    # Eliminar los caracteres con categoría 'Mn' (diacríticos)
    texto_sin_diacriticos = ''.join(char for char in texto_normalizado if unicodedata.category(char) != 'Mn')
    return texto_sin_diacriticos

def vocal_mas_comun(texto):

    texto = normalizar_texto(texto)
    texto = texto.lower()

    vocales = ['a', 'e', 'i', 'o', 'u']
    most = 0
    letra = ''

    for vocal in vocales:
        if texto.count(vocal) > most:
            most = texto.count(vocal)
            letra = vocal

    return letra
        

texto = 'Hola buenos dias mi nombre es Arnau Nin Pérez'
print(vocal_mas_comun(texto))