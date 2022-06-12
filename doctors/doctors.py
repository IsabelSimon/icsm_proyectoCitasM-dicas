import mysql.connector
import datetime
import hashlib
import doctors.conexion as conexion

#llamar la clase conectar
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Doctor:
    
    def __init__(self, nombre, apellidos, cedula, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cedula = cedula
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO doctores VALUES(null, %s, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.cedula, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0,self]
        
        return result

    def identificar(self):
        # Login de usuarios
        sql = "SELECT * FROM doctores WHERE email = %s AND password = %s"

        #cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #datos para consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result