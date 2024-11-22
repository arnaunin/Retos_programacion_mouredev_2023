import numpy as np

def comprar_producto(dinero, num_producto):
    cambio = np.array([], int)
    monedas_soportadas = [200, 100, 50, 10, 5]
    productos = {
    1: {"nombre": "Agua", "precio": 150},
    2: {"nombre": "Refresco", "precio": 100},
    3: {"nombre": "Chocolate", "precio": 200},
    4: {"nombre": "Galletas", "precio": 50},
    5: {"nombre": "Chicle", "precio": 120},
    6: {"nombre": "Caramelos", "precio": 75},
    7: {"nombre": "Café", "precio": 180},
    8: {"nombre": "Té", "precio": 90},}
    
    # No existe el producto
    if num_producto not in productos.keys():
        print("ERROR: el número de producto no existe")
        return dinero
    
    # Existe el producto
    else:
        precio_producto = productos[num_producto]["precio"] # Precio del producto
        nombre_producto = productos[num_producto]["nombre"] # Nombre del producto
        # Las monedas introducidas no estan dentro de las soportadas
        for moneda in dinero:
            if moneda not in monedas_soportadas:
                print("ERROR: se han introducido monedas no soportadas por la maquina")
                return
        
        # Caso en el que el dinero es insuficiente
        if dinero.sum() < precio_producto:
            print("ERROR: el dinero introducido es insuficiente")
            return dinero
        
        # Caso en el que el dinero es suficiente o exacto
        elif dinero.sum() >= precio_producto:
            # Calculamos el cambio
            cambio_total = dinero.sum() - precio_producto
            for monedas in monedas_soportadas:
                while cambio_total >= monedas:
                    cambio = np.append(cambio, monedas)
                    cambio_total -= monedas
                
            return (nombre_producto, cambio)


dinero = np.array([50, 100, 5, 10, 5], int)
print(comprar_producto(dinero, 1))