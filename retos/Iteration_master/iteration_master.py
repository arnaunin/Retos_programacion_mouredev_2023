# Con un bucle for
print("BUCLE FOR:")

for i in range(1, 101):
    print(i)

# Con un bucle while
print("BUCLE WHILE:")

i = 1
while i <= 100:
    print(i)
    i += 1

# De forma recursiva
print("FORMA RECURSIVA:")

def imprimir_numeros(n):
    if n == 0:
        return
    else:
        imprimir_numeros(n-1)
        print(n)
    
imprimir_numeros(100)

# Con comprensión de listas
print("COMPRENSIÓN DE LISTAS:")

[print(i) for i in range(1, 101)]

# Con una función generadora
print("FUNCION GENERADORA:")

def funcion_generadora():
    for i in range(1, 101):
        yield i

for numero in funcion_generadora():
    print(numero)

# Usando el metodo map()
print("METODO MAP")

numeros = list(map(print, range(1, 101)))

