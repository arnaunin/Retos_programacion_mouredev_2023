def ley_de_ohm(V=None, R=None, I=None):

    # Guardamos los paramentros en una lista
    valores = [V, R, I]
    proporcionados = [valor for valor in valores if valor is not None] # Comprobamos cuantos de los valores se han proporcionado

    # Si se han introducido menos de dos o mas de dos retornamos 'Invalid values'
    if len(proporcionados) != 2:
        return "Invalid values"
    
    # Si se han introducido dos parametros comprobamos que sean de tipo int o float
    if not all(isinstance(v, (int, float)) for v in proporcionados):
        return "Invalid values"
    
    # Si se han introducido dos paramentros y los tipos de los dos son correctos hacemos los calculos para saber cuanto vale el tercer parametro
    if V is None:
        return round(I * R, 2)
    
    elif R is None:
        if I == 0:
            return "Invalid values"
        return round(V / I, 2)
    
    elif I is None:
        if R == 0:
            return "Invalid values"
        return round(V / R, 2)

print(ley_de_ohm(V=10, I=2))          
print(ley_de_ohm(V=10, R="cinco"))    
print(ley_de_ohm(V=None, R=None, I=None))
print(ley_de_ohm(V=10, R=0)) 