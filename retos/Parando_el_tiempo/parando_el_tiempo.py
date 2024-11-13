# Este código ejecuta varias tareas a la vez y las imprime en el orden que finalizan

import asyncio

# Definimos la coroutine
async def parando_el_tiempo(num1, num2, tiempo, tarea):
    await asyncio.sleep(tiempo)  # Pausa asíncrona sin bloquear
    print(f"Tarea {tarea}: {num1 + num2}")

# Creamos una función principal para manejar las coroutines
async def main():
    # Creamos las tareas
    tareas = [
        asyncio.create_task(parando_el_tiempo(1, 3, 2, 1)),  # Tarea 1 con 2 segundos de espera
        asyncio.create_task(parando_el_tiempo(2, 1, 1, 2)),  # Tarea 2 con 1 segundo de espera
        asyncio.create_task(parando_el_tiempo(3, 2, 3, 3))   # Tarea 3 con 3 segundos de espera
    ]
    
    # Esperamos que las tareas finalicen (sin esperar a que terminen en orden)
    for tarea in tareas:
        await tarea  # Imprime automáticamente cuando termina cada tarea

# Ejecutamos la función principal
asyncio.run(main())
