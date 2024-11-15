# En python se pueden definir los arrays de tres formas:
#   - Con listas de python, en las que solo se contenga variables de un solo tipo
#   - Con el modulo array que nos permite crear arrays que solo pueden contener variables de un solo tipo
#   - Con la biblioteca NumPy, para arrays multidimensionales y mas complejas
# En este caso vamos a usar las listas de python como arrays ya que es un ejercicio sencillo

def  conjuntos(array1, array2, booleano):

    # Si el booleano tiene valor True
    if booleano:
        array_final = [elemento for elemento in array1 if elemento in array2] # Añadimos los elementos de array1 que también estan en array2 (los comunes)
    # Si tiene valor False
    else:
        array_final = [elemento for elemento in array1 if elemento not in array2] # Añadimos los elementos de array1 que no estan en array2 (los no comunes)7
        array_final.extend([elemento for elemento in array2 if elemento not in array1]) # Añadimos los elemetnos de array2 que no estan en array 1

    return array_final

array1 = [1,2,3,4,5,6,7,8,9]
array2 = [10,11,12,13,1,2,3,4]
booleano = False

print(conjuntos(array1, array2, booleano))