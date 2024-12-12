# La libreria random nos es util para generar los dulces o los sustos aleatorios
import random

def  truco_trato(accion, personas):

    sustos = ['🎃', '👻', '💀', '🕷', '🕸', '🦇']
    dulces = ['🍰', '🍬', '🍡', '🍭', '🍪', '🍫', '🧁', '🍩']

    if accion == 'truco':
        
        # Calculamos cuantos sustos hay por los nombres de las personas
        sustos_letras = sum(len(persona['nombre'])//2 for persona in personas)

        # Calculamos cuantos sustos hay por las edades
        sustos_edades = len([persona['edad'] for persona in personas if persona['edad'] % 2 == 0]) * 2

        # Calculamos los sustos por la altura total de todas las personas
        sustos_alturas = (sum(persona['altura'] for persona in personas) // 100 ) * 3

        # Sustos totales
        sustos_totales = sustos_letras + sustos_edades + sustos_alturas

        # Generamos una lista con sustos aleatorios de una longitud igual al numero de sustos_totales
        sustos = random.choices(sustos, k=sustos_totales)

        return sustos

    elif accion == 'trato':

        # Calculamos los dulces que salen por las letras de los nombres
        dulces_nombres = sum(len(nombre['nombre']) for nombre in personas)

        # Calculamo los dulces que salen por los años de los niños
        dulces_anios = sum(min(persona['edad'] // 3, 3) for persona in personas)

        # Calculamos cuantos dulces salen por la altura de cada persona
        dulces_altura = sum(min(persona['altura'] // 50, 3) for persona in personas) * 2

        # Dulces totales
        dulces_totales = dulces_altura + dulces_nombres + dulces_anios

        # Generamos una lista con sustos aleatorios de una longitud igual al numero de sustos_totales
        dulces = random.choices(dulces, k=dulces_totales)

        return dulces

    else:
        return "ERROR: la accion introducida no es valida"


personas = [
    {"nombre": "Ana", "edad": 8, "altura": 130},
    {"nombre": "Luis", "edad": 10, "altura": 140},
    {"nombre": "Marta", "edad": 6, "altura": 120},
    {"nombre": "Carlos", "edad": 12, "altura": 150},
]

accion = 'trato'

print(truco_trato(accion, personas))

