from cmath import log
import doctors.doctors as modelo
import citas.acciones

class Acciones:

    def registro(self):
        print("Se procedera a realizar tu registro en el sistema...")

        nombre = input("Nombre(s): ")
        apellidos = input("Apellidos: ")
        cedula = input("Cédula: ")
        email = input("Email: ")
        password = input("Contraseña: ")


        doctor = modelo.Doctor(nombre,apellidos, cedula, email,password)
        registro = doctor.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto se ha registrado a {registro[1].nombre} con éxito, con el email {registro[1].email}")
        else:
            print("\nNo se realizó el registro correctamente")

    def login(self):
        print("\nIdentifiquese en el sistema...")

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            doctor = modelo.Doctor('', '','', email, password)
            login = doctor.identificar()

            if email == login[4]:
                print(f"Bienvenido {login[1]}, te has logeado en el sistema el {login[6]}")
                self.proximasAcciones(login)
           
        except Exception as e:
            print("Algo salió mal, intente de nuevo")

    def proximasAcciones(self, doctor):
        print("""
        Acciones disponibles:
            - Crear cita (crear)
            - Mostrar citas (mostrar)
            - Editar cita (editar)
            - Eliminar cita (eliminar)
            - Salir (salir)
        """)

        accion = input("¿Qué desea hacer?: ")
        hazEl  = citas.acciones.Acciones()
        
        if accion == "crear":
            hazEl.crear(doctor)
            self.proximasAcciones(doctor)
        
        elif accion == "mostrar":
            hazEl.mostrar(doctor)
            self.proximasAcciones(doctor)

        elif accion == "editar":
            hazEl.editar(doctor)
            self.proximasAcciones(doctor)

        elif accion == "eliminar":
            hazEl.borrar(doctor)
            self.proximasAcciones(doctor)

        elif accion == "salir":
            exit()
        else:
            print("Opción no disponible, elija nuevamente")
            self.proximasAcciones(doctor)
        return None
        