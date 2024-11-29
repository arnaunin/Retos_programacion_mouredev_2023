def ataque_pokemon(atacante, defensor, ataque, defensa):

    tipos = ['agua', 'fuego', 'planta', 'electrico']

    # Comprovamos que los parámetros pasados a la función son válidos
    if atacante not in tipos or defensor not in tipos or ataque not in range(1, 101) or defensa not in range(1, 101):
        return "ERROR: los parámetros introducidos no son validos"
    
    efectividades = {'agua': {'agua': 0.5, 'fuego': 2, 'planta': 0.5, 'electrico': 1},
                   'fuego': {'agua': 0.5, 'fuego': 0.5, 'planta': 2, 'electrico': 1},
                   'planta': {'agua': 2, 'fuego': 0.5, 'planta': 0.5, 'electrico': 1},
                   'electrico': {'agua': 2, 'fuego': 1, 'planta': 0.5, 'electrico': 0.5}}
    
    efectividad = efectividades[atacante][defensor]

    damage = 50 * (ataque/defensa) * efectividad

    return f"El daño que inflinge el pokémon de tipo {atacante} al pokémon de tipo {defensor} es de {damage:.2f} puntos de vida"

atacante = 'fuego'
defensor = 'electrico'
ataque = 95
defensa = 75

print(ataque_pokemon(atacante, defensor, ataque, defensa))
