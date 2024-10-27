from sistema_colegio import Curso, Colegio, Profesor, Alumno, Persona
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
    print("12. Asignar Calificaciones")
    print("13. Informacion Cursos")
    print("14. Notas Segun Alumno")
    print("15. Notas Segun Curso")
    print("16. Salir")

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
    id = input("Ingrese el ID del profesor: ")
    rut = input("Ingrese el RUT del profesor: ")
    nombre = input("Ingrese el nombre del profesor: ")
    apellido = input("Ingrese el apellido del profesor: ")
    correo = input("Ingrese el correo del profesor: ")
    especializacion = input("Ingrese la especializacion del profesor: ")
    profesor = Profesor(id, rut, nombre, apellido, correo, especializacion)
    colegio.agregar_profesor(profesor)

def agregar_alumno():
    id = input("Ingrese el ID del alumno: ")
    rut = input("Ingrese el RUT del alumno: ")
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    correo = input("Ingrese el correo del alumno: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno: ")
    alumno = Alumno(id, rut, nombre, apellido, correo, fecha_nacimiento)
    colegio.agregar_alumno(alumno)


def inscribir_curso(self, curso: Curso):
    if curso.codigo not in self.cursos_inscritos:
        self.cursos_inscritos[curso.codigo] = curso
    else:
        print(f"El alumno {self.id} ya está inscrito en el curso {curso.nombre}.")

def inscribir_alumno_a_curso():
    alumno_id = input("Ingrese el ID del alumno: ")
    codigo_curso = input("Ingrese el codigo del curso: ")
    alumno = next((a for a in colegio.alumnos if a.id == alumno_id), None)
    curso = next((c for c in colegio.cursos if c.codigo == codigo_curso), None)
    if alumno and curso:
        alumno.inscribir_curso(curso)
        print(f"Alumno {alumno.nombre} inscrito en el curso {curso.nombre}.")
    else:
        print("Alumno o curso no encontrado.")

def asignar_calificacion(self, alumno_id, curso_codigo, calificacion):
        alumno = next((a for a in self.alumnos if a.id == alumno_id), None)
        curso = next((c for c in self.cursos if c.codigo == curso_codigo), None)
        if alumno and curso:
            if curso_codigo in alumno.cursos_inscritos:
                alumno.calificaciones[curso_codigo] = calificacion
                print(f"Calificación {calificacion} asignada a {alumno.nombre} en el curso {curso.nombre}.")
            else:
                print(f"El alumno {alumno.nombre} no está inscrito en el curso {curso.nombre}.")
        else:
            print("Alumno o curso no encontrado.")

def asignar_profesor_a_curso():
    id_profesor = input("Ingrese el ID del profesor: ")
    codigo_curso = input("Ingrese el código del curso: ")
    profesor = next((p for p in colegio.profesores if p.id == id_profesor), None)
    curso = next((c for c in colegio.cursos if c.codigo == codigo_curso), None)
    if profesor and curso:
        colegio.asignar_profesor_a_curso(profesor, curso)
    else:
        print("El profesor o el curso no existen en el colegio")
        

def asignar_calificacion():
    id_alumno = input("Ingrese el ID del alumno: ")
    codigo_curso = input("Ingrese el código del curso: ")
    while True:
        try:
            calificacion = float(input("Ingrese la calificación del alumno: "))
            if calificacion > 7 or calificacion < 1:
                print("Nota no válida. Ingrese nota entre 1.0 y 7.0")
            else:
                break
        except ValueError:
            print("Error de ingreso. Ingrese nota entre 1.0 y 7.0")
    alumno = next((a for a in colegio.alumnos if a.id == id_alumno), None)
    curso = next((c for c in colegio.cursos if c.codigo == codigo_curso), None)
    if alumno and curso:
        alumno.registrar_calificaciones(curso, calificacion)
    else:
        print("El alumno o el curso no existen en el colegio")

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
        agregar_profesor()
        pausa()

    elif opcion == "5":
        id = input("Ingrese el id del profesor a eliminar: ")
        colegio.eliminar_profesor(id)
        pausa()

    elif opcion == "6":
        colegio.mostrar_informacion_profesores()
        pausa()

    elif opcion == "7":
        agregar_alumno()
        pausa()

    elif opcion == "8":
        id = input("Ingrese el id del alumno a eliminar: ")
        colegio.eliminar_alumno(id)
        pausa()

    elif opcion == "9":
        colegio.mostrar_informacion_alumnos()
        pausa()

    elif opcion == "10":
        asignar_profesor_a_curso()
        pausa()

    elif opcion == "11":
        inscribir_alumno_a_curso()
        pausa()

    elif opcion == "12":
        asignar_calificacion()
        pausa()

    elif opcion == "13":
        colegio.informacion_cursos()
        pausa()

    elif opcion == "14":
        colegio.notas_segun_alumno()
        pausa()

    elif opcion == "15":
        colegio.notas_segun_curso()
        pausa()

    elif opcion == "16":
        print("Fin")
        break

    else:
        print("Opción no válida, intente de nuevo.")
        pausa()
