```markdown
# Guardians of the Ancient Kingdom

Este es un proyecto académico desarrollado en Python que simula un juego de batallas por turnos en la terminal. El objetivo principal de este proyecto es demostrar la aplicación práctica de los **4 pilares de la Programación Orientada a Objetos (POO)**.

## Características del Juego
* **Creación interactiva:** Permite elegir entre 3 tipos de personajes (Guerrero, Mago, Arquero) y asignarles sus puntos de vida, ataque y defensa.
* **Sistema de turnos:** Batallas interactivas donde cada personaje ataca hasta que la vida de uno llega a 0.
* **Habilidades Especiales:** Cada clase tiene una forma única de calcular su daño durante el combate.

## Conceptos de POO Aplicados

1. **Abstracción y Encapsulamiento:**
   * Se creó una clase base llamada `Personaje`.
   * Los atributos (`__vida`, `__ataque`, `__defensa`) son **privados** para proteger la integridad de los datos.
   * Se utilizan métodos `getters` y `setters` para acceder a ellos. El método `set_vida()` incluye un condicional que asegura que la salud nunca sea menor a 0 ni mayor a 100.

2. **Herencia:**
   * Las clases `Guerrero`, `Mago` y `Arquero` heredan de la clase principal `Personaje`, reutilizando sus atributos y métodos básicos para no repetir código.

3. **Polimorfismo:**
   * El método `atacar()` está presente en todas las clases, pero cada personaje hace una matemática diferente al usarlo:
     * **Guerrero:** Su ataque tiene un 20% de incremento de daño.
     * **Mago:** Su ataque ignora por completo la defensa del objetivo.
     * **Arquero:** Si su ataque es mayor que la defensa del objetivo, hace el doble de daño.

## Cómo ejecutar el juego

1. Asegúrate de tener Python instalado en tu computadora.
2. Descarga el archivo principal de Python (ej. `GuardiansOfTheAcientKingdom.py`).
3. Abre una terminal o línea de comandos en la carpeta donde guardaste el archivo.
4. Ejecuta el siguiente comando:
   ```bash
   python GuardiansOfTheAcientKingdom.py