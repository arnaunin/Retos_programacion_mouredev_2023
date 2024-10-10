def area_poligono(poligono):
    try:
        if poligono == "cuadrado":
            lado = int(input("Introduce el tamaño de los lados: "))
            area = lado*lado
            return area
        elif poligono == "rectangulo":
            ancho = int(input("Introduce el tamaño del ancho: "))
            largo = int(input("Introduce el tamaño del largo: "))
            area = ancho*largo
            return area
        elif poligono == "triangulo":
            base = int(input("Introduce el tamaño de la base: "))
            altura = int(input("Introduce el tamaño de la altura: "))
            area = (base*altura)/2
            return area
    except:
        print(ValueError)

print(area_poligono("triangulo"))
print(area_poligono("cuadrado"))
print(area_poligono("rectangulo"))
