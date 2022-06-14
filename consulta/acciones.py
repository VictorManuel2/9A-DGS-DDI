import consulta.consultas as modelo

class Acciones:
    
    def agregar(self, doctor):
        print(f"{doctor[6]} {doctor[1]} --- Agregue una consulta...")

        nombre_paciente = input("Introduce el nombre del paciente: ")
        telefono = input("Introduce su numero de telefono: ")
        edad = input("Indrocute su edad: ")
        

        consulta = modelo.Consulta(doctor[0], nombre_paciente, telefono, edad)
        guardar = consulta.agregar()

        if guardar[0] >= 1:
            print(f"\n Se ha guardado correctamente la consulta de: {consulta.nombre_paciente}")
        
        else:
            print(f"\nNo se guardo la consulta, intentalo mas tarde: {doctor[1]}")

    def mostrar(self, doctor):
        print(f"\n {doctor[6]} {doctor[1]} ---- Estas son sus consultas: ")

        consulta = modelo.Consulta(doctor[0])
        consultas = consulta.listar()

        #print(notas)
        if consultas:
           for consulta in consultas:
            print("****************************************") 
            print(f"""
            Paciente: {consulta[2]}
            telefono: {consulta[3]}
            edad: {consulta[4]} años
            """)
            print("****************************************") 
    def actualizar(self, doctor):
        print(f"{doctor[6]} {doctor[1]} ---- Modifique la consulta")

        nombre_paciente = input("Introduce el nombre del paciente: ")

        consulta = modelo.Consulta(doctor[0], nombre_paciente)
        validar = consulta.validar()

        if validar[0] != 0:
            self.modificar(doctor, nombre_paciente)
        else:
            print(f"\nParece que no hay una consulta agendada para ese paciente, intentao más tarde: {doctor[1]}")

    def modificar(self, doctor, nombre):
        print(f"{doctor[6]} {doctor[1]}!!! Escriba los nuevos datos del paciente {nombre}")

        nombre_paciente = input("Introduce el nuevo nombre del paciente: ")
        telefono = input("Escribe el nuevo telefono: ")
        edad = input("Escribe la edad: ")

        consulta = modelo.Consulta(doctor[0], nombre_paciente, telefono, edad, nombre)
        guardar = consulta.actualizar()
        if guardar[0] >= 1:
            print(f"\nSe han modificado los datos del paciente: {consulta.nombre_paciente}")
        else:
            print(f"\nNo se encontró ninguna consulta con el nombre del pacientte [{nombre_paciente}], verifique si los datos son correctos")
    
    def eliminar(self, doctor):
        print(f"\n {doctor[6]} {doctor[1]} ------ Borrar una consulta agendada")
        nombre_paciente = input("Introduce el nombre del paciente para eliminar consulta: ")

        nota = modelo.Consulta(doctor[0], nombre_paciente)
        eliminar = nota.eliminar()
        if eliminar[0] >= 1:
            print(f"Se eliminó la consulta de: {nota.nombre_paciente}")
        else:
            print("No se puedo eliminar la consulta, intenta más tarde...")
    