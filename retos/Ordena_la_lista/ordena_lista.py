def ordena_lista(lista, orden):
    # Si la lista esta vacía la retornamos tal cual
    if not lista:
        return lista

    # En caso contrario la ordenamos
    else:
        lista_ordenada = []

        if orden == "Asc":
            while lista:
                menor = min(lista)
                lista_ordenada.append(menor)
                lista.remove(menor)
                
        elif orden == "Desc":
            while lista:
                mayor = max(lista)
                lista_ordenada.append(mayor)
                lista.remove(mayor)

        return lista_ordenada

lista = [3,5,2,4,9,8,3]
print(ordena_lista(lista, 'Desc'))
