#Bienvenidos a la evaluacion 2 en GitHub!
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa():
    input("Presione Enter para continuar...")

def mostrar_menu():
    limpiar_pantalla()
    print("\nSistema de Gestión Escolar")
    print("1. Agregar Curso")
    print("2. Eliminar Curso")
    print("3. Listar Cursos")
    print("4. Agregar Profesor")
    print("5. Eliminar Profesor")
    print("6. Listar Profesores")
    print("7. Agregar Alumno")
    print("8. Eliminar Alumno")
    print("9. Listar Alumnos")
    print("10. Asignar Profesor a Curso")
    print("11. Inscribir Alumno a Curso")
    print("12. Registrar Calificaciones")
    print("13. Mostrar información completa de los cursos")
    print("14. Salir")
