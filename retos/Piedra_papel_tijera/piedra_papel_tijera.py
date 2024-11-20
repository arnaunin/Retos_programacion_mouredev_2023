def piedra_papel_tijera(partidas):
    combinaciones = {("R","P"): 2, ("R","R"): 0, ("R","S"): 1,
                     ("P","P"): 0, ("P","R"): 1, ("P","S"): 2,
                     ("S","P"): 1, ("S","R"): 2, ("S","S"): 0}
    
    # contadores
    jugador1 = 0
    jugador2 = 0

    # recorremos la lista con todas las partidas i comprovamos los resultados
    for partida in partidas:
        resultado = combinaciones[partida]
        if resultado == 1:
            jugador1 += 1
        elif resultado == 2:
            jugador2 += 1

    # imprimimos el resultado final

    if jugador1 > jugador2:
        return 'Player 1'
    elif jugador1 < jugador2:
        return 'Player 2'
    elif jugador1 == jugador2:
        return 'Tie'


partidas = [("R","S"), ("S","R"), ("P","S")]
print(piedra_papel_tijera(partidas))