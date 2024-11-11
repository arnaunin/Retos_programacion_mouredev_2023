# La carrera de obstáculos

Crea una función que evalúe si un/a atleta ha superado correctamente una carrera de obstáculos.
- La función recibirá dos parámetros:
    - Un array que sólo puede contener String con las palabras "run" o "jump"
    - Un String que represente la pista y sólo puede contener "_" (suelo) o "|"     (valla)
- La función imprimirá cómo ha finalizado la carrera:
    - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no variará el símbolo de esa parte de la pista.
    - Si hace "jump" en "_" (suelo), se variará la pista por "x".
    - Si hace "run" en "|" (valla), se variará la pista por "/".
- La función retornará un Boolean que indique si ha superado la carrera.
Para ello tiene que realizar la opción correcta en cada tramo de la pista.

#

Create a function to determine if an athlete successfully completed an obstacle course.
- The function will receive two parameters:
    - An array that only contains strings with the words "run" or "jump".
    - A string representing the course, which can only contain "_" (ground) or "|" (hurdle).
- The function will display how the course ended based on the athlete's actions:
    - If the athlete does "run" on "_" (ground) and "jump" on "|" (hurdle), the action is correct, and the course symbol will remain unchanged for that part of the track.
    - If the athlete does "jump" on "_" (ground), that part of the course will be changed to "x".
    - If the athlete does "run" on "|"   (hurdle), that part of the course will be changed to "/".

- The function will return a Boolean indicating whether the athlete successfully completed the course. 
To successfully complete the course, the athlete must make the correct action at each segment of the course.

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
   python carrera_obstaculos.py
   ```
   o
   ```
   python3 carrera_obstaculos.py
