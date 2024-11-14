import operator

def calculadora_txt(ruta_al_fichero):
    # Leemos la información del fichero i la guardamos en la variable content
    try:
        with open(ruta_al_fichero, "r") as my_file:
            content = my_file.read()
    except FileNotFoundError:
        print("El archivo no se encontró en la ruta especificada.")

    # Separamos la información por lineas
    lineas = content.splitlines()

    # Diccionario con las operaciones posibles
    operaciones = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv,}

    # Variables que usaremos para almacenar los valores del fichero .txt
    resultado = 0
    operador = operator.add

    # Antes de recorrer el fichero miramos que la ultima linea de el sea un número, en caso contario imprimimos un mensaje de error i terminamos la ejecucion de código
    if not lineas[-1].isdigit():
        print("ERROR: No se han podido resolver las operaciones")
        return

    # Recorremos cada linea con un indice por linea
    for i, valor in enumerate(lineas): # Si el indice es par el valor de la linea debe ser un numero si es impar un operando, si esto no ocurre se mostrará un mensaje de error

        # Caso en el que valor debería ser un número
        if i % 2 == 0 and valor.isdigit():
            resultado = operador(resultado, int(valor))

        # Caso en el que el valor debería ser un operando
        elif i % 2 != 0 and valor in operaciones.keys():
            operador = operaciones[valor]

        # Caso en el que no ocurre ninguna de las dos cosas
        else:
            print("ERROR: No se han podido resolver las operaciones")
            return
        
    print("Resultado:", resultado)

calculadora_txt("retos/Calculadora_txt/Challenge21.txt")