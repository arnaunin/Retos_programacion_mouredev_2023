from datetime import datetime

def tiempo_entre_juegos():

    zelda_juegos = [('The Legend of Zelda', '21/02/1986'),
    ('Zelda II: The Adventure of Link', '14/01/1987'),
    ('The Legend of Zelda: A Link to the Past', '21/11/1991'),
    ('The Legend of Zelda: Link\'s Awakening', '06/06/1993'),
    ('The Legend of Zelda: Ocarina of Time', '21/11/1998'),
    ('The Legend of Zelda: Majora\'s Mask', '27/04/2000'),
    ('The Legend of Zelda: Oracle of Seasons', '27/02/2001'),
    ('The Legend of Zelda: Oracle of Ages', '27/02/2001'),
    ('The Legend of Zelda: Four Swords', '02/12/2002'),
    ('The Legend of Zelda: The Wind Waker', '13/12/2002'),
    ('The Legend of Zelda: Four Swords Adventures', '18/03/2004'),
    ('The Legend of Zelda: The Minish Cap', '04/11/2004'),
    ('The Legend of Zelda: Twilight Princess', '19/11/2006'),
    ('The Legend of Zelda: Phantom Hourglass', '23/06/2007'),
    ('The Legend of Zelda: Spirit Tracks', '07/12/2009'),
    ('The Legend of Zelda: Skyward Sword', '20/11/2011'),
    ('The Legend of Zelda: A Link Between Worlds', '22/11/2013'),
    ('The Legend of Zelda: Tri Force Heroes', '22/10/2015'),
    ('The Legend of Zelda: Breath of the Wild', '03/03/2017'),
    ('The Legend of Zelda: Link\'s Awakening (Remake)', '20/09/2019'),
    ('The Legend of Zelda: Tears of the Kingdom', '12/05/2023')]

    print(len(zelda_juegos))
    print(range(len(zelda_juegos)))
   
    # Imprimimos todos los juegos
    for i in range(len(zelda_juegos)):
        print(f"{i}. {zelda_juegos[i][0]}")

    # Pedimos al ususario que escoja dos juegos
    print()
    print("Escoge dos jugeos de Zelda por sus indices para saber cuanto tiempo ha pasado entre sus lanzamientos:")

    # Si el ususario no introduce números saltará un ValueError
    try:
        primero = int(input("Primer juego: "))
        segundo = int(input("Segundo juego: "))
    except ValueError:
        return "ValueError: los valores introducidos no son válidos"
    
    # Si ha introducido números pero no estan en el rango que los indices de los juegos también saltará un error
    if primero not in range(len(zelda_juegos)) or segundo not in range(len(zelda_juegos)):
        return "IndexError: los valores introducidos no están en la lista"

    # Si lo valores son válidos el codigo continua

    # Guardamos los nombres y las fechas de los juegos elegidos
    juego_1 = zelda_juegos[primero][0]
    juego_2 = zelda_juegos[segundo][0]
    fecha_1 = datetime.strptime(zelda_juegos[primero][1], "%d/%m/%Y")
    fecha_2 = datetime.strptime(zelda_juegos[segundo][1], "%d/%m/%Y")

    intervalo = fecha_1 - fecha_2
    intervalo = abs(intervalo).days

    # Años completos y días restantes
    anios_completos = intervalo // 365
    dias_restantes = intervalo % 365

    return f"Entre los lanzamientos de {juego_1} y {juego_2} hay una diferencia de {anios_completos} años y {dias_restantes} dias."



print(tiempo_entre_juegos())