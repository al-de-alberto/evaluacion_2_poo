
from sistema_colegio import Curso, Colegio, Profesor, Alumno
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
    print("13. Generar reporte")
    print("14. Salir")

colegio = Colegio()

def agrega_curso():
    codigo = input("Ingrese el código del curso: ")
    nombre = input("Ingrese el nombre del curso: ")

def agregar_profesor():
    id = input("Ingrese el id del profesor: ")
    nombre = input("Ingrese el nombre del profesor: ")
    especializacion = input("Ingrese la especializacion del profesor: ")

def agregar_alumno():
    id = input("Ingrese el id del alumno: ")
    nombre = input("Ingrese el nombre del alumno: ")
