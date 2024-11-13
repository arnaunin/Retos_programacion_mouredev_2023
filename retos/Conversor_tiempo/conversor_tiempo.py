def conversor(dias, horas, minutos, segundos):
    milisegundos = segundos*1000 + minutos*60000 + horas*3600000 + dias*86400000
    return milisegundos

print(conversor(2,12,34,54))