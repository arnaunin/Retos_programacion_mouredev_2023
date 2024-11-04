def eliminar_caracteres(str1, str2):

    out1 = ''.join(caracter for caracter in str1 if caracter not in str2)
    out2 = ''.join(caracter for caracter in str2 if caracter not in str1)

    print('Out1:', out1)
    print('Out2:', out2)

eliminar_caracteres('python','caracteres')