def es_primo(n):
    for i in range(2, n):
        if n % i == 0: # Si la división de ese numero por algun otro numero da 0, el numero no puede ser primo y se retorna False
            return False
    
    return True # Si ha completado el bucle significa que no tiene ningún dividendo a parte de 1 y el mismo por lo tanto es primo

for i in range(2, 101):
    if es_primo(i):
        print(i)

