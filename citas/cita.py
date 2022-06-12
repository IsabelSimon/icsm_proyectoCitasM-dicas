import doctors.conexion as conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Cita:
    def __init__(self, doctor_id, consultorio_id="", paciente="", hora="", fecha_cita="", notas=""):
        self.doctor = doctor_id
        self.consultorio = consultorio_id
        self.paciente = paciente
        self.hora = hora
        self.fecha_cita = fecha_cita
        self.notas = notas

    def guardar(self):
        sql = "INSERT INTO citas VALUES(null, %s, %s, %s, %s, %s, NOW(), %s)"
        cita = (self.doctor,self.consultorio,self.paciente,self.hora,self.fecha_cita,self.notas)
        cursor.execute(sql,cita)
        database.commit()
        return [cursor.rowcount, self]
   
    def listar(self):
        sql = f"SELECT C.*, R.consultorio FROM citas C INNER JOIN consultorios R ON C.consultorio_id = R.id WHERE C.doctor_id = {self.doctor}; "
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def editarNombre(self,id,nombre):
        sql = f"UPDATE citas SET paciente = '{nombre}' WHERE id = {id};"
        cursor.execute(sql)  
        database.commit()
        return[cursor.rowcount, self]

    def editarConsultorio(self,id,consultorio):
        sql = f"UPDATE citas SET consultorio_id = {consultorio} WHERE id = {id};"
        cursor.execute(sql)  
        database.commit()
        return[cursor.rowcount, self]

    def editarHora(self,id,hora):
        sql = f"UPDATE citas SET hora = '{hora}' WHERE id = {id};"
        cursor.execute(sql)  
        database.commit()
        return[cursor.rowcount, self]

    def editarFecha(self,id,fecha):
        sql = f"UPDATE citas SET fecha_cita = '{fecha}' WHERE id = {id};"
        cursor.execute(sql)  
        database.commit()
        return[cursor.rowcount, self]

    def editarNotas(self,id,notas):
        sql = f"UPDATE citas SET notas = '{notas}' WHERE id = {id};"
        cursor.execute(sql)  
        database.commit()
        return[cursor.rowcount, self]
    

    def eliminar(self,id):
        sql = f"DELETE FROM citas WHERE id = {id};"
        cursor.execute(sql)  
        database.commit()

        return[cursor.rowcount, self]