def equilibrada(expresion):
   
   # Diccionario que mapea delimitadores abiertos a cerrados
    delimitadores = {'{':'}', '[':']', '(':')'}
    pila = []

    for caracter in expresion:
        if caracter in delimitadores:  # Si es un delimitador abierto
            pila.append(caracter)
        elif caracter in delimitadores.values():  # Si es un delimitador cerrado
            if not pila or delimitadores[pila.pop()] != caracter:
                return False  # No hay coincidencia o la pila está vacía

    return not pila  # Si la pila está vacía, es equilibrada

print(equilibrada("{ [ a * ( c + d ) ] - 5 }"))  # Debería devolver True

