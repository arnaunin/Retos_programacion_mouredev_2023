def bumeranes(secuencia):

    bumeranes = [[secuencia[i], secuencia[i+1], secuencia[i+2]] for i in range(len(secuencia)-2) if secuencia[i] == secuencia[i+2]]

    print("Bumeranes encontrados: ", bumeranes)

    return len(bumeranes)

secuencia = [2, 1, 2, 3, 3, 4, 2, 4, 2]

print("Numero de bumeranes: ", bumeranes(secuencia))