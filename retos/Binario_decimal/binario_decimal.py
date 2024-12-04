def binario_a_decimal(numero):
    
    lenght = len(str(numero)) - 1

    decimal = sum(2**i for i, digito in zip(range(lenght, -1, -1), str(numero)) if digito == '1')

    return decimal

print(binario_a_decimal(10111))


