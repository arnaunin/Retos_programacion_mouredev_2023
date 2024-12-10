# Para elegir el pivote vamos a hacer la mediana de tres valores, el primero, el último i el del medio
# Esto reduce la probabilidad de un mal rendimiento, incluso para listas parcialmente ordenadas
# Para calcular la mediana vamos a utilizar una función auxiliar que implementaremos

def mediana_de_tres(valor1, valor2, valor3):
    
    if (valor1 <= valor2 <= valor3) or (valor3 <= valor2 <= valor1):
        return valor2
    elif (valor2 <= valor1 <= valor3) or (valor3 <= valor1 <= valor2):
        return valor1
    else:
        return valor3

def quick_sort(lista):

    if len(lista) <= 1:

        return lista

    pivote = mediana_de_tres(lista[0], lista[-1], lista[len(lista)//2])
    lista.remove(pivote)

    menores = [valor for valor in lista if valor <= pivote] # Lista con lo valores menores o iguales que el pivote
    mayores = [valor for valor in lista if valor > pivote] # Lista con los valores mayores que el pivote 

    return quick_sort(menores) + [pivote] + quick_sort(mayores)


lista = [7,3,4,6,1,10,2,3,17,9]
print(quick_sort(lista))

