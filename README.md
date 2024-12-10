# Gestión de Campeones de League of Legends

Este proyecto es un programa interactivo que permite gestionar una lista de campeones de **League of Legends**. 
Con este sistema, los usuarios pueden agregar, eliminar, buscar y listar campeones, todo desde una interfaz en la terminal.


![Portada de League of Legends](imagenes/portada_lol.jpg)


## Funcionalidades

1. **Agregar Campeones**:
   - Ingresa el nombre del campeón y su rol (Top, Jungla, Mid, ADC, Soporte).
   - Validar que el nombre solo contenga letras, espacios o apóstrofes.
   - No permite duplicados.

2. **Eliminar Campeones**:
   - Elimina un campeón de la lista mediante su nombre.
   - Ignora mayúsculas/minúsculas para facilitar el manejo de datos.
   - Solicita confirmación antes de eliminar.

3. **Buscar Campeones**:
   - Encuentra campeones en la lista ingresando su nombre.
   - Muestra el nombre y rol del campeón si existe.

4. **Mostrar Campeones**:
   - Lista todos los campeones almacenados con sus roles en formato numerado.

5. **Salir**:
   - Finaliza el programa.

---

## Estructura del Proyecto

El código está dividido en dos archivos:

- **`funciones_campeones.py`**: Contiene todas las funciones del programa, como agregar, eliminar, buscar, mostrar campeones y el menú principal.
- **`main.py`**: Importa y ejecuta la función principal (`menu()`) para iniciar el programa.

---

## Tecnologías Utilizadas

- **Lenguaje**: Python 3.10 o superior.
- **Estructuras de datos**: Listas y Diccionarios.

---

## Requisitos Previos

1. Tener Python 3 instalado. 

## Como usar el código

Abrir el archivo main.py y ejecutar el código.

Integrantes del equipo:
-CHIODIN, Lucas Ezequiel (Team Lead)
-COCERES, Francisco Lautaro
-FRANETOVICH, María Pía
-IZQUIERDO, Luciana 

