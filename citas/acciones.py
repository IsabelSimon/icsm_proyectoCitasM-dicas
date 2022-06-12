import citas.cita as modelo
import consultorios.consultorio as consultorio

class Acciones:

    def crear(self, doctor):
        print(f"Creando una cita\n")

        consulta = consultorio.Consultorio(doctor)       
        consultorios =  consulta.listar()   

        print("Consultorios disponibles:\n")
        for consul in consultorios:
            print(f"({consul[0]}) {consul[1]}")

        no_consultorio = input("\nEscriba solo el número del consultorio: ")
        paciente = input("Agregue el nombre del paciente: ")
        hora = input("Indique hora de la cita (formato HH:MM:SS): ")
        fecha_cita = input("Indique la fecha de la cita (formato YYYY-MM-DD): ")
        notas = input("Agregue notas adicionales: ")
      
        cita = modelo.Cita(doctor[0],int(no_consultorio),paciente,hora,fecha_cita,notas)
        
        guardar = cita.guardar()

        if guardar[0] >= 1:
            print(f"\n¡Perfecto! Has guardado la cita para el día: {cita.fecha_cita} ")
        else:
            print(f"\n {doctor[1]} No se guardo la cita, intente más tarde")

    def mostrar(self,doctor):
        print (f"\n {doctor[1]}  Estas son sus citas: ")
        cita = modelo.Cita(doctor[0])
        citas = cita.listar()
        if not citas:
            print("\n No tiene citas aún")
        else:
            for cita in citas:
                print("\n*************************")
                print(f"Consultorio: {cita[8]}")
                print(f"Paciente: {cita[3]}")
                print(f"Fecha: {cita[5]}")
                print(f"Hora: {cita[4]}")
                print(f"Notas: {cita[7]}")
                print("****************************")
    
    def editar(self,doctor):
        print (f"\n Elige solo el número de la cita a editar: ")
        cita = modelo.Cita(doctor[0])
        citas = cita.listar()
        for cita in citas:
            print("\n*************************")
            print(f"({cita[0]}) -> número de cita")
            print(f"Consultorio: {cita[8]}")
            print(f"Paciente: {cita[3]}")
            print(f"Fecha: {cita[5]}")

        no_cita = input("\nIntroduce número de cita que desea editar: ")
        citaP = modelo.Cita(cita[0])

        print("""
        \n ¿Qué deseas editar?:
            - (1) Nombre paciente 
            - (2) Consultorio 
            - (3) Hora
            - (4) Fecha 
            - (5) Notas 
            - (6) Salir
        """)
        eleccion = input("Introduce número del campo que deseas editar: ")
        print(citaP.hora)
        if(eleccion == "1"):
            nombre = input("Introduce nombre del paciente: ")
            editar = citaP.editarNombre(no_cita,nombre)
        elif(eleccion == "2"):
            consultorio = input("Introduce número de consultorio: ")
            editar = citaP.editarConsultorio(no_cita,int(consultorio))

        elif(eleccion == "3"):
            hora = input("Introduce hora de la cita (formato HH:MM:SS): ")
            editar = citaP.editarHora(no_cita,hora)
        elif(eleccion == "4"):
            fecha = input("Indique la fecha de la cita (formato YYYY-MM-DD): ")
            editar = citaP.editarFecha(no_cita,fecha)
        elif(eleccion == "5"):
            notas = input("Escriba sus notas para esta consulta: ")
            editar = citaP.editarNotas(no_cita,notas)
        elif(eleccion == "6"):
            exit()
        else:
            print("Opción no disponible, elija otra...")
            del no_cita
            self.editar(doctor)

        if(editar[0] >= 1):
            print(f"\n Cita numero {no_cita} editada")
        else:
            print("No se pudo editar nota, intente más tarde")

    def borrar(self,doctor):
        print(f"{doctor[1]} !! Estás por borrar una cita")
        print (f"\n Elige solo el número de la cita a eliminar: ")
        cita = modelo.Cita(doctor[0])
        citas = cita.listar()
        for cita in citas:
            print("\n*************************")
            print(f"Cita número: {cita[0]}")
            print(f"Consultorio: {cita[8]}")
            print(f"Paciente: {cita[3]}")
            print(f"Fecha: {cita[5]}")

        no_cita = input("Introduce número de cita: ")
        cita = modelo.Cita(cita[0])
        eliminar = cita.eliminar(no_cita)

        if(eliminar[0] >= 1):
            print(f"Cita número {no_cita} eliminada")
        else:
            print("No se pudo eliminar cita, intente más tarde")