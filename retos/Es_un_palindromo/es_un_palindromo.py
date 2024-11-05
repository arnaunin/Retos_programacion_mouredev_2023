import string as str

def palindromo(texto):
    # Variable que contiene el texto sin espacios, signos de puntuación o tildes
    texto_limpio = ''.join(letra.lower() for letra in texto if letra in str.ascii_letters)

    if texto_limpio == texto_limpio[::-1]:
        return True
    else:
        return False
    
print(palindromo('Ana lleva al oso la avellana.'))