def calcular_resultado(bondadosos, malvados):

    razas_bondadosas = {'Pelosos': 1, 'Sureños buenos': 2, 'Enanos': 3, 'Numenoreanos': 4, 'Elfos': 5}
    razas_malvadas = {'Sureños malos': 2, 'Orcos': 2, 'Goblins': 2, 'Huargos': 3, 'Trolls': 5}

    # Puntos de cada ejercito
    pt_bondadosos = sum(cantidad * razas_bondadosas[raza] for raza, cantidad in bondadosos.items())
    pt_malvados = sum(cantidad * razas_malvadas[raza] for raza, cantidad in malvados.items())

    return pt_bondadosos, pt_malvados
    

def batalla_tierra_media(bondadosos, malvados):

    # Calculamos la puntuación de cada ejercito
    fuerza_bondadosos, fuerza_malvados = calcular_resultado(bondadosos, malvados)

    if fuerza_bondadosos > fuerza_malvados:
        return 'Gana el bien!'
    
    elif fuerza_bondadosos < fuerza_malvados:
        return 'Gana el mal!'
    
    else:
        return 'Empate'

ejercito_bondadoso = {'Pelosos': 7, 'Sureños buenos': 4, 'Enanos': 11, 'Numenoreanos': 2, 'Elfos': 15}
ejercito_malvado = {'Sureños malos': 4, 'Orcos': 5, 'Goblins': 12, 'Huargos': 5, 'Trolls': 7}

print(batalla_tierra_media(ejercito_bondadoso, ejercito_malvado))