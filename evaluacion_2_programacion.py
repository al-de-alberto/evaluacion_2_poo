
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
    descripcion = input("Ingrese descripción del curso: ")
    while True:
        try:
            creditos = int(input("Ingrese el número de creditos del curso: "))
            break
        except:
            print("Error de ingreso")
    curso = Curso(codigo, nombre, descripcion, creditos)
    colegio.agregar_curso(curso)

def agregar_profesor():
    id = input("Ingrese el id del profesor: ")
    rut = ("Ingrese el rut del profesor: ")
    nombre = input("Ingrese el nombre del profesor: ")
    apellido = ("Ingrese el apellido del profesor: ")
    correo = ("Ingrese el correo del profesor: ")
    especializacion = input("Ingrese la especializacion del profesor: ")
    profesor = Profesor(id, rut, nombre, apellido, correo, especializacion)
    colegio.agregar_profesor(profesor)

def agregar_alumno():
    id = input("Ingrese el id del alumno: ")
    rut = ("Ingrese el rut del alumno: ")
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = ("Ingrese el apellido del alumno: ")
    correo = ("Ingrese el correo del alumno: ")
    fecha_nacimiento = ("Ingrese la fecha de nacimiento del alumno: ")
    alumno = Alumno(id, rut, nombre, apellido, correo, fecha_nacimiento)
    colegio.agregar_alumno(alumno)









while True:
    mostrar_menu()
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        agrega_curso()
        pausa()

    elif opcion == "2":
        codigo = input("Ingrese el código del curso a eliminar: ")
        colegio.eliminar_curso(codigo)
        pausa()

    elif opcion == "3":
        colegio.mostrar_informacion_cursos()
        pausa()

    elif opcion == "4":
        agrega_profesor()
        pausa()

    elif opcion == "5":
        id = input("Ingrese el id del profesor a eliminar: ")
        colegio.eliminar_profesor(id)
        pausa()

    elif opcion == "6":
        colegio.mostrar_informacion_profesores()
        pausa()

    elif opcion == "7":
        agrega_alumno()
        pausa()

    elif opcion == "8":
        id = input("Ingrese el id del alumno a eliminar: ")
        colegio.eliminar_alumno(id)
        pausa()

    elif opcion == "9":
        colegio.mostrar_informacion_alumnos()
        pausa()

    elif opcion == "10":
        asigna_profesor_a_curso()
        pausa()

    elif opcion == "11":
        inscribe_alumno_a_curso()
        pausa()

    elif opcion == "12":
        registra_calificacion()
        pausa()

    elif opcion == "13":
        colegio.mostrar_informacion_completa_cursos()
        pausa()

    elif opcion == "14":
        print("Fin")
        break
    else:
        print("Opción no válida.")
        pausa()


 
