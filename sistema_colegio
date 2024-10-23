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
        else:
            print(f"No se encontró el profesor con el id {id}")

    def eliminar_alumno(self, id):
        alumno = next((a for a in self.alumnos if a.id == id), None)
        if alumno:
            self.alumnos.remove(alumno)
        else:
            print(f"No se encontró el alumno con el id {id}")

    def asignar_profesor():

class Curso:
    def __init__(self, codigo: int, nombre: str, descripcion: str, creditos: int):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.creditos = creditos

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

    def inscribir_curso(self, curso: Curso):
        if curso.codigo not in self.cursos_inscritos:
            self.cursos_inscritos[curso.codigo] = []
        else:
            print(f"El alumno {self.id} ya esta inscrito en el curso")
        
class Profesor(Persona):
    def __init__(self, id: int, rut: str, nombre: str, apellido: str, correo: str, especializacion: str):
        super().__init__(id, rut, nombre, apellido, correo)
        
