import datetime
import hashlib #Cifrar contraseñas en Python
import doctores.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Doctor:
    def __init__(self, nombre, apellidos, cedula, telefono, consultorio, especialidad, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cedula = cedula
        self.telefono = telefono
        self.consultorio = consultorio
        self.especialidad = especialidad
        self.email = email
        self.password = password
    
    def registrar(self):
        cifrado = hashlib.sha256() # Cifrar contraseña
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO doctor VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s)"
        doctor = (self.nombre, self.apellidos, self.cedula, self.telefono, self.consultorio, self.especialidad, self.email, cifrado.hexdigest())

        try:
            cursor.execute(sql, doctor)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        return result

    def login(self):
        sql = "SELECT * FROM doctor WHERE email = %s AND password = %s"
        cifrado = hashlib.sha256() # Cifrar contraseña
        cifrado.update(self.password.encode('utf8'))

        doctor = (self.email, cifrado.hexdigest())
        cursor.execute(sql, doctor)
        result = cursor.fetchone()
        return result