import re

def conversor_temperatura(temperatura):
    # Definimos un patron que debe tener la entrada
    patron = r"^\d+(\.\d+)?º[CF]$"

    # Si la entrada no es válida se retorna un errror
    if not re.fullmatch(patron, temperatura):
        return "ERROR: el valor introducido no es válido"
    
    grados = re.search(r"\d+(\.\d+)?", temperatura).group()

    if '.' in grados:
        grados = float(grados)
    else:
        grados = int(grados)

    if 'C' in temperatura:
        return f"{((grados * 9/5) + 32):.2f} ºF"
    
    elif 'F' in temperatura:
        return f"{((grados - 32) / 9*5):.2f} ºC"
    
print(conversor_temperatura('101ºF'))