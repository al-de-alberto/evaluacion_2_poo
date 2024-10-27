from datetime import date

class Colegio:
    def __init__(self):
        self.cursos = []
        self.profesores = []
        self.alumnos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)
    
    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def mostrar_informacion_cursos(self):
        print("\nCursos disponibles")
        for curso in self.cursos:
            print(f"\nCódigo: {curso.codigo} \nNombre: {curso.nombre} \nDescripcion: {curso.descripcion} \nCreditos: {curso.creditos}")

    def mostrar_informacion_profesores(self):
            print("\nListado Profesores")
            for profesor in self.profesores:
                print(f"\nID: {profesor.id} \nRUT: {profesor.rut} \nNombre: {profesor.nombre} \nApellido: {profesor.apellido} \nCorreo: {profesor.correo} \nEspecialización: {profesor.especializacion}")

    def mostrar_informacion_alumnos(self):
        print("\nListado Alumnos")
        for alumno in self.alumnos:
            print(f"\nID: {alumno.id} \nRUT: {alumno.rut}\nNombre: {alumno.nombre} \nApellido: {alumno.apellido} \nCorreo: {alumno.correo} \nFecha Nacimiento: {alumno.fecha_nacimiento}")
    
    def eliminar_curso(self, codigo):
        curso = next((c for c in self.cursos if c.codigo == codigo), None)
        if curso:
            self.cursos.remove(curso)
        else:
            print(f"No se encontró el curso con código {codigo}")

    def eliminar_profesor(self, id):
        profesor = next((p for p in self.profesores if p.id == id), None)
        if profesor:
            self.profesores.remove(profesor)
            print(f"Profesor {profesor.nombre} eliminado.")
        else:
            print(f"No se encontró el profesor con id {id}")

    def eliminar_alumno(self, id):
        alumno = next((a for a in self.alumnos if a.id == id), None)
        if alumno:
            self.alumnos.remove(alumno)
        else:
            print(f"No se encontró el alumno con el id {id}")
    
    def listado_cursos(self):
        print('\nListado cursos')
        for curso in self.cursos:
            print(f'\nCodigo: {curso.codigo} \nNombre: {curso.nombre} \nDescripcion: {curso.descripcion} \nCreditos: {curso.creditos}')
    
    def asignar_profesor_a_curso(self, profesor, curso):
        if profesor in self.profesores and curso in self.cursos:
            profesor.asignar_curso(curso)   

    def inscribir_alumno_a_curso(self, alumno, curso):
        if alumno in self.alumnos and curso in self.cursos:
            alumno.cursos_inscritos(curso)   
        
    def informacion_cursos(self):
        print("\nCursos disponibles:\n")
        for curso in self.cursos:
            profesor_asignado = None
            alumnos_inscritos = None
            for profesor in self.profesores:
                if curso in profesor.cursos_asociados:
                    profesor_asignado = profesor.nombre
                    break

            alumnos_inscritos = []
            for alumno in self.alumnos:
                if curso.codigo in alumno.cursos_inscritos:
                    alumnos_inscritos.append(alumno.nombre)

            print(f"Nombre: {curso.nombre}, Créditos: {curso.creditos}")
            print(f"Profesor Asignado: {profesor_asignado}")
            print(f"Alumnos Inscritos: {', '.join(alumnos_inscritos)}")
            print("-" * 30)

    def notas_segun_alumno(self):
        pass

    def notas_segun_curso(self, alumno):
        print("\nReporte de notas:")
        print(alumno.calificacion)


class Curso:
    def __init__(self, codigo: int, nombre: str, descripcion: str, creditos: int):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.creditos = creditos
        self.profesor = None

class Persona:
    def __init__(self, id: int, rut: str, nombre: str, apellido: str, correo: str):
        self.id = id
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

class Alumno(Persona):
    def __init__(self, id: int, rut: str, nombre: str, apellido: str, correo: str, fecha_nacimiento: date):
        super().__init__(id, rut, nombre, apellido, correo)
        self.fecha_nacimiento = fecha_nacimiento
        self.cursos_inscritos = {}  
        self.calificaciones = {}

    def inscribir_curso(self, curso: Curso):
        if curso.codigo not in self.cursos_inscritos:
            self.cursos_inscritos[curso.codigo] = [] 
        else:
            print(f"El alumno {self.id} ya está inscrito en el curso {curso.nombre}.")

    def registrar_calificaciones(self, curso, calificacion):
        if curso.codigo in self.cursos_inscritos:
            self.cursos_inscritos[curso.codigo].append(calificacion)
        else:
            print(f"El alumno no está inscrito en el curso {curso.codigo}")

    

            
class Profesor(Persona):
    def __init__(self, id: int, rut: str, nombre: str, apellido: str, correo: str, especializacion: str):
        super().__init__(id, rut, nombre, apellido, correo)
        self.especializacion = especializacion
        self.cursos_asociados = []        

    def asignar_curso(self, curso: Curso):
        self.cursos_asociados.append(curso)
