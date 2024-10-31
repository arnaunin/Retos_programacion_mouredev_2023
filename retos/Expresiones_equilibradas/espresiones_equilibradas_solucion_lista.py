def equilibrada(expresion):
    equilibrada = True
    # Guardamos todos los delimitadores en una lista
    delimitadores = [caracter for caracter in expresion if caracter in "{}[]()"] # Comprension de listas

    # Caso en el que no hay delimitadores
    if not delimitadores:
        return True # Es una expresion equilibrada
    # Caso en el que hay delimitadores
    else:
        # Si el numero de delimitadores es impar es que la expresion no esta equilibrada
        if len(delimitadores) % 2 != 0:
            return False
        # Caso en el que hay un numero de delimitadores par
        else:
            # Recorremos la mitad de la lista y comparamos con el delimitador con el que deberia corresponder
            for i, delimitador in enumerate(delimitadores[:int(len(delimitadores)/2)]):
                if delimitador == "(":
                    if not delimitadores[len(delimitadores)-i-1] == ")":
                        return False
                elif delimitador == "[":
                    if not delimitadores[len(delimitadores)-i-1] == "]":
                        return False
                elif delimitador == "{":
                    if not delimitadores[len(delimitadores)-i-1] == "}":
                        return False
                return True

print(equilibrada("{ a * ( c + d ) ] - 5 }"))