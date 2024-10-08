def fibonacci(n):

    # Inicializamos los dos primeros valores de la sucessión
    a = 0 # Pirmer valor
    b = 1 # segundo valor

    # Vamos a recorrer el bucle n veces para imprimir los n primeros valores
    for i in range(n):
        print(f"{i+1}: {a}")
        a, b = b, a + b # El primer valor pasa a ser el segundo valor y el segundo pasa a ser la suma del primero y el segundo

fibonacci(50)