# Batalla pokémon

Crea un programa que calcule el daño de un ataque durante una batalla Pokémon.
- La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad 
- Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
- Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico (buscar su efectividad)
- El programa recibe los siguientes parámetros:
    - Tipo del Pokémon atacante.
    - Tipo del Pokémon defensor.
    - Ataque: Entre 1 y 100.
    - Defensa: Entre 1 y 100.

#

Create a program to calculate the damage of an attack during a Pokémon battle.
- The formula will be as follows: damage = 50 * (attack / defense) * effectiveness
- Effectiveness: x2 (super effective), x1 (neutral), x0.5 (not very effective)
- There are only 4 Pokémon types: Water, Fire, Grass, and Electric (look up their effectiveness).
- The program receives the following parameters:
    - Attacking Pokémon type.
    - Defending Pokémon type.
    - Attack: Between 1 and 100.
    - Defense: Between 1 and 100.

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
   python batalla_pokemon.py
   ```
   o
   ```
   python3 batalla_pokemon.py