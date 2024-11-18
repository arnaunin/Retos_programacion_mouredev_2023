def mcd(a, b):
    # Utilizaremos el algoritmo de Euclides paraa calucular el mcd ya que es mas eficiente
    while b != 0:
        a,b = b, a % b

    return a
                

def mcm(c, d):
    # Utilizamos la formula para calular el mcm y nos apoyamos de la función del mcd
    MCM = abs(c * d) / mcd(c, d)

    return int(MCM)


print(mcd(45,36))
print(mcm(22,12))

