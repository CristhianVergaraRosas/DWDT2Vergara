from alumnos import alumno

if __name__=='__main__':
    alumnosSistema = []

print("Bienvenidos al Registro de Notas")
while True:

    print("--------------------------------")
    print("Lista de comandos")
    print("R: Registrar          C: Calificar")
    print("M: Mostrar Notas      S: Sumar Notas")
    print("P: Promediar Notas    X: Sumar Notas")

    comandoInformacion = input("Ingrese un comando : ")
    print(f"El comando ingresado es {comandoInformacion}")

    match comandoInformacion:
        case "R":
            print("Se registrará un nuevo producto: ")
            nombreAlumno = input("Ingrese el nombre del alumno : ")
            apellidoAlumno = input("Ingrese el apellido del alumno : ")
            edadAlumno = input("Ingrese la edad del alumno : ")
            nacionalidadAlumno = input("Ingrese la nacionalidad del alumno : ")
            objAlumno = alumno(nombreAlumno, apellidoAlumno, edadAlumno, nacionalidadAlumno)
            alumnosSistema.append(objAlumno)
            print("------Alumno Registrado------")
        case "C":
            for alumnoInfo in alumnosSistema:
                notaAlumno = ''
                while not alumnoInfo.notaAlumno.isdigit():
                    notaAlumno = input(f"Alumno {alumnoInfo.nombreAlumno} {alumnoInfo.apellidoAlumno}, Ingrese Nota : ")
                    if notaAlumno.isdigit():
                        if float(notaAlumno)  >= 0 and float(notaAlumno) <= 20:
                            alumno.registrarNota(alumnoInfo, notaAlumno)
                            break
            print("--Calificaciones registradas--")
        case "S":
            notaValida = False
            notaCantidad = 0
            notaSuma = 0
            for alumnoInfo in alumnosSistema:
                notaValida = alumnoInfo.notaAlumno.isdigit()
                if not alumnoInfo.notaAlumno.isdigit():
                    break
                else:
                    notaCantidad = notaCantidad + 1
                    notaSuma = notaSuma + float(alumnoInfo.notaAlumno)

            if notaValida:
                print(f"La suma de notas para {notaCantidad} alumnos es: {notaSuma}")
            else:
                print("--Existen alumnos sin califación--")
        case "P":
            notaValida = False
            notaCantidad = 0
            notaSuma = 0
            for alumnoInfo in alumnosSistema:
                notaValida = alumnoInfo.notaAlumno.isdigit()
                if not alumnoInfo.notaAlumno.isdigit():
                    break
                else:
                    notaCantidad = notaCantidad + 1
                    notaSuma = notaSuma + float(alumnoInfo.notaAlumno)

            if notaValida:
                print(f"El promedio de notas para {notaCantidad} alumnos es: {notaSuma/notaCantidad}")
            else:
                print("--Existen alumnos sin califación--")
        case "M":
            print("Se mostrará la información de los alumnos")
            i = 0
            for alumnoInfo in alumnosSistema:
                i = i + 1
                print(f"Mostrando información del alumno {i}")
                print(f"Alumno : {alumnoInfo.nombreAlumno} {alumnoInfo.apellidoAlumno}, Edad: {alumnoInfo.edadAlumno} , Nacionalidad: {alumnoInfo.nacionalidadAlumno}")
                print(f"Nota : {alumno.leerNota(alumnoInfo)} ")
                print("\n")
        case "X":
            print("Comando de finalización")
            break
        case _:
            print("Comando incorrecto, vuelva a ingresarlo")
    #else:
        