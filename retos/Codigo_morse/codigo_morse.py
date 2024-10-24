import string as str

# Diccionarios de equivalencias

letras_a_morse = {
    'a': '.-',    'b': '-...',  'c': '-.-.',  'ch': '----',  'd': '-..',  'e': '.',
    'f': '..-.',  'g': '--.',   'h': '....',  'i': '..',    'j': '.---',
    'k': '-.-',   'l': '.-..',  'm': '--',    'n': '-.',    'ñ': '--.--', 'o': '---',
    'p': '.--.',  'q': '--.-',  'r': '.-.',   's': '...',   't': '-',
    'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',  'y': '-.--',
    'z': '--..',  '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
    '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.',  ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', 
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}


morse_a_letras = {v: k for k, v in letras_a_morse.items()} # Invierte los valores del primer diccionario usando una comprensión de diccionario

# Funcion transformador del input que se le pase al programa
def transformar(input):
    primera = input[0].lower()

    if primera in str.ascii_lowercase:
        conversion = texto_a_morse(input)

    else:
        conversion = morse_a_texto(input)

    return conversion

# Funcion que transforma de texto a codigo morse
def texto_a_morse(texto):
    
    codigo = '' # Varaible donde se va a ir almacenando la trducción a codigo morse
    i = 0 # Variable que controla los indices de las letras

    while i < len(texto): # Recorremos caracter por caracter todo el texto i sus respectivas posiciones

        letra = texto[i].lower()

        # Nos aseguramos de que no estamos en la ultima letra i que la letra en la que estamos es una 'ch'
        if i < len(texto) - 1 and letra == 'c' and texto[i+1].lower() == 'h':
            codigo += ('----'+ ' ')
            i += 1
        
        # Si encontramos un espacio en el texto 
        elif letra == ' ':
            codigo += ' ' # Añadimos dos espacios en el codigo morse

        # Si no es ni una ch ni un espacio se trata de otro caracter
        else:
            codigo += (letras_a_morse[letra]+ ' ') # Lo añadimos precedido de un espacio a la string del codigo

        i += 1

    return codigo


# Funcion que transforma de codigo morse a texto
def morse_a_texto(codigo):

    texto = '' # Varible donde se va a ir alamacenando la traduccion a texto

    lista_codigo = [palabra.split() for palabra in codigo.split('  ')] # Creamos una lista de listas con las palabras y cada una de las letrass de cada palabra

    # Recorremos la lista de listas
    for palabra in lista_codigo:
        for letra in palabra:
            texto += (morse_a_letras[letra])

        texto += ' ' # Al final de cada palabra añadimos un espacio

    return texto

print(transformar('Hola mundo'))