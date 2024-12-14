# ¿Dónde está el robot?

Calcula dónde estará un robot (sus coordenadas finales) que se encuentra en una cuadrícula representada por los ejes "x" e "y".

- El robot comienza en la coordenada `(0, 0)`.
- Para indicarle que se mueva, le enviamos un array formado por enteros (positivos o negativos) que indican la secuencia de pasos a dar.
- Por ejemplo: `[10, 5, -2]` indica que primero se mueve 10 pasos, se detiene, luego 5, se detiene, y finalmente 2.  
  El resultado en este caso sería `(x: -5, y: 12)`.
- Si el número de pasos es negativo, se desplazará en sentido contrario al que está mirando.
- Los primeros pasos los hace en el eje `y`. Interpretamos que está mirando hacia la parte positiva del eje `y`.
- **El robot tiene un fallo en su programación**: cada vez que finaliza una secuencia de pasos, gira 90 grados en el sentido contrario a las agujas del reloj.

#

Calculate where a robot (its final coordinates) will be in a grid represented by the "x" and "y" axes.

- The robot starts at coordinate `(0, 0)`.
- To instruct it to move, we send it an array of integers (positive or negative) indicating the sequence of steps to take.
- For example: `[10, 5, -2]` means it moves 10 steps, stops, then 5 steps, stops, and finally 2 steps.  
  The result in this case would be `(x: -5, y: 12)`.
- If the number of steps is negative, the robot moves in the opposite direction it is facing.
- The first steps are made along the `y` axis, assuming it is initially facing the positive `y` direction.
- **The robot has a programming error**: after completing a sequence of steps, it turns 90 degrees counterclockwise.

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
   python donde_esta_el_robot.py
   ```
   o
   ```
   python3 donde_esta_el_robot.py
