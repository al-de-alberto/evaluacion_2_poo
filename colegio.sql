-- Elimina base datos colegio_db
DROP DATABASE IF EXISTS colegio_db;
-- Crear la base de datos colegio_db
CREATE DATABASE colegio_db;
USE colegio_db;

-- Tabla para almacenar información de cursos
CREATE TABLE cursos (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    descripcion TEXT,
    creditos INT
);

-- Tabla para almacenar información de profesores
CREATE TABLE profesores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rut VARCHAR(45) NOT NULL,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    correo VARCHAR(45) NOT NULL,
    especializacion VARCHAR(45)
);

-- Tabla para almacenar información de alumnos
CREATE TABLE alumnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rut VARCHAR(45) NOT NULL,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    correo VARCHAR(45) NOT NULL,
    fecha_nacimiento DATE
);

-- Tabla de relación entre cursos y profesores (para asignar profesores a cursos)
CREATE TABLE cursos_profesores (
    curso_codigo INT,
    profesor_id INT,
    FOREIGN KEY (curso_codigo) REFERENCES cursos(codigo),
    FOREIGN KEY (profesor_id) REFERENCES profesores(id)
);

-- Tabla de relación entre cursos y alumnos (para inscribir alumnos en cursos)
CREATE TABLE cursos_alumnos (
    curso_codigo INT,
    alumno_id INT,
    FOREIGN KEY (curso_codigo) REFERENCES cursos(codigo),
    FOREIGN KEY (alumno_id) REFERENCES alumnos(id)
);

-- Tabla para almacenar calificaciones de alumnos en cursos
CREATE TABLE calificaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    curso_codigo INT,
    alumno_id INT,
    calificacion DECIMAL(2, 1),
    FOREIGN KEY (curso_codigo) REFERENCES cursos(codigo),
    FOREIGN KEY (alumno_id) REFERENCES alumnos(id)
);
INSERT INTO cursos (nombre, descripcion, creditos) VALUES ('POO','Programación Orientada a Objeto',3);
INSERT INTO cursos (nombre, descripcion, creditos) VALUES ('FRONT END','Programación Front End',3);
SELECT * FROM cursos;
INSERT INTO alumnos (rut, nombre, apellido, correo, fecha_nacimiento) VALUES ('111-1','Alan','Brito','abrito@gmail.com','2000-12-12');
INSERT INTO alumnos (rut, nombre, apellido, correo, fecha_nacimiento) VALUES ('222-2','Luis','Tapia','ltapia@gmail.com','2000-11-11');
SELECT * FROM alumnos;
INSERT INTO profesores (rut, nombre, apellido, correo, especializacion) VALUES ('333-3','Juan','Perez','jperez@gmail.com','Programación');
INSERT INTO profesores (rut, nombre, apellido, correo, especializacion) VALUES ('444-4','Carolina','Soto','csoto@gmail.com','Diseño Web');
SELECT * FROM profesores;
INSERT INTO cursos_alumnos (curso_codigo, alumno_id) VALUES (1, 1);
INSERT INTO cursos_alumnos (curso_codigo, alumno_id) VALUES (1, 2);
INSERT INTO cursos_alumnos (curso_codigo, alumno_id) VALUES (2, 1);

SELECT alumnos.id, alumnos.nombre, alumnos.fecha_nacimiento FROM alumnos INNER JOIN cursos_alumnos ON alumnos.id = cursos_alumnos.alumno_id WHERE cursos_alumnos.curso_codigo = 1;

INSERT INTO cursos_profesores (curso_codigo, profesor_id) VALUES (1, 1);
INSERT INTO cursos_profesores (curso_codigo, profesor_id) VALUES (2, 1);
SELECT * FROM cursos_profesores;
SELECT cursos.codigo, cursos.nombre, profesores.nombre FROM cursos inner JOIN cursos_profesores ON cursos.codigo = cursos_profesores.curso_codigo  inner JOIN profesores ON cursos_profesores.profesor_id = profesores.id;
