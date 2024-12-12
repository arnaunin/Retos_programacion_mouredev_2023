# Truco o trato

Este es un reto especial por Halloween.
Deberemos crear un programa al que le indiquemos si queremos realizar "Truco o Trato" y un listado (array) de personas con las siguientes propiedades:
- Nombre de la niña o niño
- Edad
- Altura en centímetros

Si las personas han pedido truco, el programa retornará sustos (aleatorios) siguiendo estos criterios:
- Un susto por cada 2 letras del nombre por persona
- Dos sustos por cada edad que sea un número par
- Tres sustos por cada 100 cm de altura entre todas las personas
- Sustos: 🎃 👻 💀 🕷 🕸 🦇

Si las personas han pedido trato, el programa retornará dulces (aleatorios) siguiendo estos criterios:
- Un dulce por cada letra de nombre
- Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
- Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
- Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩

En caso contrario retornará un error.

#

This is a special challenge for Halloween.  
We need to create a program where we specify whether we want "Trick or Treat" and provide a list (array) of people with the following properties:  
- Name of the child  
- Age  
- Height in centimeters  

If the people choose "trick," the program will return scares (randomly selected) following these criteria:  
- One scare for every 2 letters in the name per person  
- Two scares for each even-numbered age  
- Three scares for every 100 cm of total height among all people  
- Scares: 🎃 👻 💀 🕷 🕸 🦇  

If the people choose "treat," the program will return candies (randomly selected) following these criteria:  
- One candy for each letter in the name  
- One candy for every 3 years of age, up to a maximum of 10 candies per person  
- Two candies for every 50 cm of height, up to a maximum of 150 cm per person  
- Candies: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩  

Otherwise, it will return an error.  

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
   python truco_trato.py
   ```
   o
   ```
   python3 truco_trato.py
