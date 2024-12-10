campeones = {}

roles_validos = ["Top", "Jungla", "Mid", "ADC", "Soporte"]

def validar_nombre(nombre):
    return all(caracter.isalpha() or caracter in ["'", " "] for caracter in nombre)


def validar_rol(rol):
    return rol in roles_validos

def agregar_campeon(nombre, rol):
    nombre = nombre.title()
    rol = rol.lower()        

    if not validar_nombre(nombre):
        return "El nombre solo debe contener letras, espacios y/o apóstrofe (')."
    if rol not in [r.lower() for r in roles_validos]:
        return "El rol ingresado no es válido."
    if nombre in campeones:
        return "Ese campeón ya está en la lista."
    
    campeones[nombre] = rol.title()
    return f"Campeón {nombre} con el rol de {rol.title()} se agregó correctamente."

def eliminar_campeon(nombre):
    nombre = nombre.title()
    
    if nombre not in campeones:
        return "El campeón no está en la lista."

    confirmacion = input(f"¿Estás seguro de que deseas eliminar a {nombre}? (S/Cualquier tecla): ").lower()
    if confirmacion == "s":
        del campeones[nombre]
        return f"Campeón {nombre} eliminado correctamente."
    else:
        return "Eliminación cancelada."

def buscar_campeon(nombre):
    if nombre in campeones:
        return f"Campeón encontrado: {nombre} - Rol: {campeones[nombre]}"
    return "El campeón no está en la lista."

def mostrar_campeones():
    if not campeones:
        return "No hay campeones en la lista."
    
    resultado = "Lista de campeones:\n"
    for i, (nombre, rol) in enumerate(campeones.items(), start=1):
        resultado += f"{i} - {nombre} - {rol}\n"
    return resultado.strip()

def menu():
    while True:
        print("\nGestión de Campeones de League of Legends")
        print("1. Agregar un campeón")
        print("2. Eliminar un campeón")
        print("3. Buscar un campeón")
        print("4. Mostrar todos los campeones")
        print("5. Salir")
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "1":
            nombre = input("Ingresa el nombre del campeón: ").strip()
            rol = input("Ingresa el rol del campeón (Top, Jungla, Mid, ADC, Soporte): ").strip()
            print(agregar_campeon(nombre, rol))
        
        elif opcion == "2":
            nombre = input("Ingresa el nombre del campeón que deseas eliminar: ").strip()
            print(eliminar_campeon(nombre))
        
        elif opcion == "3":
            nombre = input("Ingresa el nombre del campeón que deseas buscar: ").strip()
            print(buscar_campeon(nombre))
        
        elif opcion == "4":
            print(mostrar_campeones())
        
        elif opcion == "5":
            print("¡Adios invocador, buena suerte!")
            break
        
        else:
            print("Opción no válida, intente de nuevo.")
