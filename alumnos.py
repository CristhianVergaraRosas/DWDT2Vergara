class alumno:
    def __init__(self, nombre, apellido, edad, nacionalidad):
        self.nombreAlumno = nombre
        self.apellidoAlumno = apellido
        self.edadAlumno = edad
        self.notaAlumno = ''
        self.nacionalidadAlumno = nacionalidad

    def registrarNota(self, notaAlumno):
        self.notaAlumno=notaAlumno

    def leerNota(self):
        return self.notaAlumno