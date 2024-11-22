# Máquina expendedora
Simula el funcionamiento de una máquina expendedora creando una operación que reciba dinero (array de monedas) y un número que indique la selección del producto.
- El programa retornará el nombre del producto y un array con el dinero de vuelta (con el menor número de monedas).
- Si el dinero es insuficiente o el número de producto no existe, deberá indicarse con un mensaje y retornar todas las monedas.
- Si no hay dinero de vuelta, el array se retornará vacío.
- Para que resulte más simple, trabajaremos en céntimos con monedas de 5, 10, 50, 100 y 200.
- Debemos controlar que las monedas enviadas estén dentro de las soportadas.

#

Simulate the operation of a vending machine by creating a function that receives money (array of coins) and a number indicating the selected product.
- The program will return the name of the product and an array with the change (using the smallest number of coins).
- If the money is insufficient or the product number does not exist, it should display a message and return all the coins.
- If there is no change, the array will be returned empty.
- To simplify, we will work in cents with coins of 5, 10, 50, 100, and 200.
- We must ensure that the coins provided are among the supported ones.

## Instalación y ejecución
1. Clona el respoitorio (si no lo has clonado ya antes con algún otro ejercicio, si ya lo has clonado ve directo al paso 3):
   ```
   https://github.com/arnaunin/Retos_programacion_mouredev_2023.git
   ```
2. Instala las dependencias necesarias (si las hay):
   ```
   pip install -r requirements.txt
   ```
3. Navega hasta el ejercicio en cuestión:
   ```
   cd path_to_repository/
   ```
4. Ejecuta el proyecto:
   ```
   python maquina_expendedora.py
   ```
   o
   ```
   python3 maquina_expendedora.py
