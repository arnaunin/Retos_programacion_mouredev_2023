def numero_amstrong(num):
    digitos = len(str(num))

    suma = sum(int(valor)**digitos for valor in str(num))

    return suma == num

print(numero_amstrong(371))