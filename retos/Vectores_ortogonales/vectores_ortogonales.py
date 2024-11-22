import numpy as np

# Dos vectores son ortogonales si su producto escalar es igual a 0

def ortogonales(vector1, vector2):
    producto_escalar = np.dot(vector1, vector2)

    return not producto_escalar

vector1 = np.array([1, 2], float)
vector2 = np.array([2, -1], float)

print(ortogonales(vector1, vector2))