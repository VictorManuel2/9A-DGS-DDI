import doctores.doctor as modelo
import consulta.acciones

class Acciones:
    def registro(self):

        print("Introduzca los siguientes datos para su registro en el sistema.")
        nombre = input("¿Cuál es su nombre?: ")
        apellidos = input("¿Cuáles son sus apellidos?: ")
        cedula = input("Ingrese su cedula profesional: ")
        telefono = input("Ingrese su numero telefonico: ")
        consultorio = input("¿Cuál es su número de consultorio?: ")
        especialidad = input("¿Cuál es su especialidad?: ")
        email = input("¿Cuál es su Email?: ")
        password = input("Introduce tu contraseña: ")

        doctor = modelo.Doctor(nombre, apellidos, cedula, telefono, consultorio, especialidad, email, password)
        registro = doctor.registrar()
        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].especialidad} {registro[1].nombre} te has registrado  con el email {registro[1].email}")
        else:
            print("\nOcurrio un error, intentelo nuevamente.")

    def login(self):
        print("\nIniciar sesión en el sistema")
        #try:
        email = input("Introduce tu Email: ")
        password = input("Introduce tu contraseña: ")

        doctor = modelo.Doctor('','','','','','',email, password)
        login = doctor.login()

        if email == login[7]:
            print(f"Bienvenid@ {login[6]} {login[1]}, has iniciado sesion con el correo {login[7]}")
            self.proximasAcciones(login)
        #except:
        print("\nLogin incorrecto vuelva a intentalo más tarde")

    def proximasAcciones(self, doctor):
        print("""
Acciones disponibles:
    - Agregar consulta (agregar)
    - Listar consultas (listar)
    - modificar consulta (modificar)
    - Eliminar consulta (eliminar)
    - Salir (salir)
""")

        accion = input("¿Qué desea realizar?: ")
        hazEl = consulta.acciones.Acciones()
        if accion == "agregar":
            hazEl.agregar(doctor)
            self.proximasAcciones(doctor) 
        elif accion == "listar":
            hazEl.mostrar(doctor)
            self.proximasAcciones(doctor)
        elif accion == "modificar":
            hazEl.actualizar(doctor)
            self.proximasAcciones(doctor)
        elif accion == "eliminar":
            hazEl.eliminar(doctor)
            self.proximasAcciones(doctor)
        elif accion == "salir":
            exit()
