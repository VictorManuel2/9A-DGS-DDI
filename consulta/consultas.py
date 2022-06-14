import doctores.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Consulta: 

    def __init__(self, doctor_id, nombre_paciente="", telefono="", edad = "", nombre = ""):
        self.doctor_id = doctor_id
        self.nombre_paciente = nombre_paciente
        self.telefono =  telefono
        self.edad = edad
        self. nombre = nombre

    def agregar(self):
        sql = "INSERT INTO consultas VALUES(null, %s, %s, %s, %s, NOW())"
        consulta = (self.doctor_id, self.nombre_paciente, self.telefono, self.edad)

        cursor.execute(sql, consulta)
        database.commit()
        return [cursor.rowcount, self]

    def listar(self):
        sql = f"SELECT * FROM consultas WHERE doctor_id = {self.doctor_id}"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def validar(self):
        sql = f"SELECT * FROM consultas WHERE nombre_paciente = '{self.nombre_paciente}'"
        cursor.execute(sql)
        return [cursor.rowcount, self]

    def eliminar(self):
        sql = f"DELETE FROM consultas WHERE doctor_id = {self.doctor_id} AND nombre_paciente = '{self.nombre_paciente}'"

        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self]

    def actualizar(self):
        sql = f"UPDATE consultas SET nombre_paciente = '{self.nombre_paciente}', telefono = '{self.telefono}', edad = {self.edad} WHERE nombre_paciente = '{self.nombre}'"

        cursor.execute(sql) 
        database.commit()

        return [cursor.rowcount, self]