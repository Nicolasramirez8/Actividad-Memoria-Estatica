"""
Mini-Sistema de Registro de Calificaciones
Autor: Nicolás Ramírez Montero
Asignatura: Tipos de Datos Abstractos (TDA)
Tema: Memoria Estática (inmutable) y Memoria Dinámica (mutable) en Python
"""

# -----------------------------------------
# Memoria Estática (Inmutable)
# -----------------------------------------

materias = ("Física", "Lectura", "Estructuras de información", "Inglés") # Tupla fija
nombre_estudiante = "Juan Naranjo" #Cadena inmutable

# -----------------------------------------
# Memoria Dinámica (Mutable)
# -----------------------------------------

calificaciones = [None for _ in materias] #Lista mutable para almacenar calificaciones

# -----------------------------------------
# Funciones del sistema
# -----------------------------------------

def menu_principal():
    """Muestra el menú principal"""
    print("\n=== Menú de calificaciones ===")
    print("1. Registrar o actualizar calificación")
    print("2. Quitar calificación")
    print("3. Consultar calificación")
    print("4. Promedio calificaciones")
    print("0. Salir")

def registrar_calificacion():
    """Permite ingresar o modificar la calificación de una materia"""
    print("\nMaterias disponibles:")
    for i, m in enumerate(materias, start=1):
        print(f"{i}, {m}")
    try:
        seleccion = int(input("Seleccione la materia: ")) - 1
        if seleccion not in range(len(materias)):
            print("Opción inválida.")
            return

        valor = float(input(f"Ingrese la calificación para {materias[seleccion]}: "))
        calificaciones[seleccion] = valor
        print(f"Calificación registrada para {materias[seleccion]} → {valor}")

    except ValueError:
        print("Debe ingresar un número válido.")

def quitar_calificacion():
    """Elimina la calificación de una materia seleccionada"""
    mostrar_calificaciones()
    try:
        seleccion = int(input("Digite el número de la materia a borrar: ")) - 1
        if seleccion not in range(len(materias)):
            print("Materia inexistente.")
            return

        if calificaciones[seleccion] is None:
            print("Esa materia no tiene calificación registrada.")
        else:
            calificaciones[seleccion] = None
            print(f"Calificación eliminada de {materias[seleccion]}")

    except ValueError:
        print("Entrada inválida.")

def mostrar_calificaciones():
    """Muestra las calificaciones actuales del estudiante"""
    print(f"\nCalificaciones de {nombre_estudiante}")
    for materia, calificaciones in zip(materia,calificaciones):
        if calificaciones is None:
            print(f" - {materia}: sin calificación")
        else:
            print(f" - {materia}: {calificaciones}")

def promedio_calificaciones():
    """Calcula y muestra el promedio de las calificaciones"""
    valores = [n for n in calificaciones if n is not None]  
    if valores:
        promedio = sum(valores) / len(valores)
        print(f"\nPromedio general: {promedio:2f}")
    else:
        print("No hay calificaciones registradas para realizar el promedio")


# -----------------------------------------
# Ejecución principal
# -----------------------------------------

def ejecutar():
    """Función principal que ejecuta el programa"""
    while True:
        menu_principal()
        opcion = input("Seleccione una opción:")

        if opcion == "1":
            registrar_calificacion
        elif opcion == "2":
            quitar_calificacion
        elif opcion == "3":
            mostrar_calificaciones
        elif opcion == "4":
            promedio_calificaciones
        elif opcion == "0":
            print("Programa finalizado")
            break
        else:
            print("Opción no válida, intente de nuevo")


if __name__ == "__main__":
    ejecutar()
