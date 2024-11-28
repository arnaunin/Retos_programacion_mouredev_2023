from itertools import cycle

def ciclo_sexagenario_chino(anio):

    elementos = ['madera', 'fuego', 'tierra', 'metal', 'agua']
    animales = ['rata', 'buey', 'tigre', 'conejo', 'dragón', 'serpiente', 'caballo', 'oveja', 'mono', 'gallo', 'perro', 'cerdo']

    if anio < 604:
        return "El ciclo sexagenario chino empezó en el año 604"
    
    animal = animales[(anio-604)%12]
    elemento = elementos[((anio-604)%10)//2]

    return (f"Animal: {animal}\nElemento: {elemento}")


print(ciclo_sexagenario_chino(2024))
